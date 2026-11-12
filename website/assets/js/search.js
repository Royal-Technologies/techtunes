/**
 * Client-Side Full-Text Search Engine for Techtunes Archive
 * Supports Bengali (বাংলা) & English search, category/author/language filters, and highlighting.
 */

(function () {
  'use strict';

  let searchIndex = [];
  let currentFilter = {
    category: 'all',
    language: 'all',
    author: '',
    query: ''
  };

  const searchInput = document.getElementById('search-input');
  const categorySelect = document.getElementById('category-filter');
  const resultsContainer = document.getElementById('search-results');
  const resultsCountElem = document.getElementById('results-count');
  const filterBtns = document.querySelectorAll('.filter-btn');

  async function initSearch() {
    try {
      const resp = await fetch('data/search-index.json');
      if (!resp.ok) throw new Error('Search index not found');
      searchIndex = await resp.json();

      populateCategoryFilter(searchIndex);

      const initialQuery = window.ArchiveUtils.getQueryParam('q');
      const initialCat = window.ArchiveUtils.getQueryParam('category');
      const initialAuthor = window.ArchiveUtils.getQueryParam('author');
      const initialLang = window.ArchiveUtils.getQueryParam('lang');

      if (initialCat && categorySelect) {
        currentFilter.category = initialCat;
        categorySelect.value = initialCat;
      }

      if (initialAuthor) {
        currentFilter.author = initialAuthor;
      }

      if (initialLang) {
        currentFilter.language = initialLang;
        updateActiveFilterUI('lang', initialLang);
      }

      if (initialQuery && searchInput) {
        searchInput.value = initialQuery;
        currentFilter.query = initialQuery;
      }

      if (initialQuery || initialCat || initialAuthor || initialLang) {
        executeSearch();
      } else if (resultsContainer) {
        renderRecentOrInitial();
      }
    } catch (err) {
      console.error('Failed to load search index:', err);
      if (resultsContainer) {
        resultsContainer.innerHTML = '<p style="text-align: center; padding: 40px; color: var(--text-muted);">Search index is currently initializing or unavailable.</p>';
      }
    }
  }

  function populateCategoryFilter(items) {
    if (!categorySelect) return;
    const catCounts = {};
    items.forEach(item => {
      (item.c || []).forEach(cat => {
        catCounts[cat] = (catCounts[cat] || 0) + 1;
      });
    });
    const sorted = Object.keys(catCounts).sort((a, b) => catCounts[b] - catCounts[a]);
    sorted.forEach(cat => {
      const opt = document.createElement('option');
      opt.value = cat;
      opt.textContent = `${cat} (${catCounts[cat]})`;
      categorySelect.appendChild(opt);
    });
  }

  function updateActiveFilterUI(type, value) {
    filterBtns.forEach(btn => {
      if (btn.dataset[type]) {
        btn.classList.toggle('active', btn.dataset[type] === value);
      }
    });
  }

  function normalizeText(str) {
    if (!str) return '';
    return str.normalize('NFC').toLowerCase().trim();
  }

  function highlightMatches(text, queryWords) {
    if (!text || queryWords.length === 0) return window.ArchiveUtils.escapeHtml(text);
    let escaped = window.ArchiveUtils.escapeHtml(text);
    queryWords.forEach(word => {
      if (word.length >= 2) {
        const regex = new RegExp(`(${word.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&')})`, 'gi');
        escaped = escaped.replace(regex, '<mark>$1</mark>');
      }
    });
    return escaped;
  }

  function executeSearch() {
    if (!resultsContainer) return;

    const rawQuery = (searchInput ? searchInput.value : '').trim();
    currentFilter.query = rawQuery;

    const normalizedQuery = normalizeText(rawQuery);
    const queryWords = normalizedQuery.split(/\s+/).filter(w => w.length > 0);

    let filtered = searchIndex;

    if (currentFilter.category !== 'all') {
      filtered = filtered.filter(item => (item.c || []).includes(currentFilter.category));
    }

    if (currentFilter.language !== 'all') {
      filtered = filtered.filter(item => item.lang === currentFilter.language);
    }

    if (currentFilter.author) {
      const targetAuthor = normalizeText(currentFilter.author);
      filtered = filtered.filter(item => normalizeText(item.a).includes(targetAuthor));
    }

    if (queryWords.length > 0) {
      filtered = filtered.map(item => {
        let score = 0;
        const titleNorm = normalizeText(item.t);
        const authorNorm = normalizeText(item.a);
        const textNorm = item.txt || '';

        queryWords.forEach(word => {
          if (titleNorm.includes(word)) score += 10;
          if (authorNorm.includes(word)) score += 6;
          if ((item.c || []).some(cat => normalizeText(cat).includes(word))) score += 5;
          if ((item.tg || []).some(t => normalizeText(t).includes(word))) score += 4;
          if (textNorm.includes(word)) score += 2;
        });

        return { item, score };
      })
      .filter(entry => entry.score > 0)
      .sort((a, b) => b.score - a.score)
      .map(entry => entry.item);
    }

    renderResults(filtered, queryWords);
  }

  function renderRecentOrInitial() {
    if (!resultsContainer) return;
    const initialList = searchIndex.slice(0, 30);
    renderResults(initialList, []);
    if (resultsCountElem) {
      resultsCountElem.textContent = `Showing latest ${initialList.length} of ${searchIndex.length} archived tunes`;
    }
  }

  function renderResults(items, queryWords) {
    if (resultsCountElem) {
      if (currentFilter.query) {
        resultsCountElem.textContent = `Found ${items.length} ${items.length === 1 ? 'tune' : 'tunes'} matching "${currentFilter.query}"`;
      } else if (currentFilter.author) {
        resultsCountElem.textContent = `Showing ${items.length} tunes by "${currentFilter.author}"`;
      } else {
        resultsCountElem.textContent = `Browsing ${items.length} archived tunes`;
      }
    }

    if (items.length === 0) {
      resultsContainer.innerHTML = `
        <div style="text-align: center; padding: 40px 20px; color: var(--text-muted);">
          <h3>কোনো টিউন পাওয়া যায়নি (No tunes found)</h3>
          <p style="margin-top: 8px;">অন্য কোনো বাংলা বা ইংরেজি শব্দ দিয়ে খুঁজুন অথবা ফিল্টার পরিবর্তন করুন।</p>
        </div>
      `;
      return;
    }

    const html = items.slice(0, 100).map(item => {
      const titleHighlighted = highlightMatches(item.t, queryWords);
      const excerptHighlighted = highlightMatches(item.ex || '', queryWords);
      const dateFormatted = window.ArchiveUtils.formatDate(item.dt);
      const primaryCat = (item.c && item.c[0]) ? item.c[0] : 'টিউনস';
      const imgSrc = item.img ? window.ArchiveUtils.resolveAssetPath(item.img) : '';

      const tagsHtml = (item.tg || []).slice(0, 3).map(t =>
        `<a href="search.html?q=${encodeURIComponent(t)}" class="tag-pill">#${window.ArchiveUtils.escapeHtml(t)}</a>`
      ).join('');

      return `
        <article class="article-card">
          ${imgSrc ? `<a href="article.html?id=${item.id}"><img src="${window.ArchiveUtils.escapeHtml(imgSrc)}" alt="${window.ArchiveUtils.escapeHtml(item.t)}" class="article-card-thumb" loading="lazy"></a>` : ''}
          <div class="article-card-body">
            <div class="article-card-meta">
              <span class="source-badge badge-techtunes">${window.ArchiveUtils.escapeHtml(primaryCat)}</span>
              <span>✍️ ${window.ArchiveUtils.escapeHtml(item.a || 'Techtunes Tuner')}</span>
              <span>•</span>
              <time>${dateFormatted}</time>
              <span>•</span>
              <span>${item.lang === 'bn' ? 'বাংলা' : 'English'}</span>
            </div>
            <h3 class="article-card-title">
              <a href="article.html?id=${item.id}">${titleHighlighted}</a>
            </h3>
            ${item.ex ? `<p class="article-card-excerpt">${excerptHighlighted}</p>` : ''}
            ${tagsHtml ? `<div class="article-card-tags">${tagsHtml}</div>` : ''}
          </div>
        </article>
      `;
    }).join('');

    resultsContainer.innerHTML = `<div class="articles-list">${html}</div>`;
  }

  if (searchInput) {
    let debounceTimer;
    searchInput.addEventListener('input', () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(executeSearch, 150);
    });
  }

  if (categorySelect) {
    categorySelect.addEventListener('change', () => {
      currentFilter.category = categorySelect.value;
      executeSearch();
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      if (lang) {
        currentFilter.language = lang;
        filterBtns.forEach(b => { if (b.dataset.lang) b.classList.remove('active'); });
        btn.classList.add('active');
      }
      executeSearch();
    });
  });

  document.addEventListener('DOMContentLoaded', initSearch);
})();
