@include('theme.default.partials.header')

<main class="theme-shell">
  <section class="hero">
    <p class="eyebrow">Fixture Home</p>
    <h1>{{ $headline ?? 'GEOFlow fixture homepage' }}</h1>
    <p>{{ $summary ?? 'A minimal homepage module for preview-first theme workflow tests.' }}</p>
  </section>

  <section class="article-list">
    @foreach (($articles ?? []) as $article)
      <article class="article-card">
        <p class="meta">{{ $article['category'] ?? 'Category' }}</p>
        <h2>{{ $article['title'] ?? 'Article title' }}</h2>
        <p>{{ $article['excerpt'] ?? 'Article excerpt placeholder.' }}</p>
      </article>
    @endforeach
  </section>
</main>

@include('theme.default.partials.footer')
