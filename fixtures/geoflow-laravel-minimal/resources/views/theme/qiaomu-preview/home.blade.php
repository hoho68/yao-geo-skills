@include('theme.qiaomu-preview.partials.header')

<main class="theme-shell">
  <section class="hero editorial-hero">
    <p class="eyebrow">Qiaomu Preview Fixture</p>
    <h1>{{ $headline ?? 'GEOFlow fixture homepage in an editorial preview shell' }}</h1>
    <p>{{ $summary ?? 'This preview keeps the fixture data contract while testing a calmer, reading-first theme direction.' }}</p>
  </section>

  <section class="article-list">
    @foreach (($articles ?? []) as $article)
      <article class="article-card editorial-card">
        <p class="meta">{{ $article['category'] ?? 'Category' }}</p>
        <h2>{{ $article['title'] ?? 'Article title' }}</h2>
        <p>{{ $article['excerpt'] ?? 'Article excerpt placeholder.' }}</p>
      </article>
    @endforeach
  </section>
</main>

@include('theme.qiaomu-preview.partials.footer')
