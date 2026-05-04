@include('theme.default.partials.header')

<main class="theme-shell article-shell">
  <article class="article-detail">
    <p class="eyebrow">{{ $article['category'] ?? 'Fixture Article' }}</p>
    <h1>{{ $article['title'] ?? 'Article title' }}</h1>
    <div class="meta">{{ $article['published_at'] ?? '2026-05-04' }}</div>
    <div class="prose">
      {!! $article['body_html'] ?? '<p>Article body placeholder.</p>' !!}
    </div>
  </article>
</main>

@include('theme.default.partials.footer')
