<?php

namespace App\Support\Site;

final class SiteThemeViewResolver
{
    public function view(string $name): string
    {
        return "theme.default.$name";
    }
}
