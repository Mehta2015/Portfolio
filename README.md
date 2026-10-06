# keyurmehta.in: static site (version 3, redesigned)

This version has the same content as version 2 with a new visual design: Newsreader and Figtree type, navy and teal colours with saffron for results, a results band under the hero, a redrawn platform diagram, and icons for services and leadership.

## Version 2 notes

This version matches the 2026 resume ("Solution Architect | Mobile, Web, Cloud & AI-Enabled Platforms"). Compared with version 1:
- The hero diagram shows the whole platform: mobile and web clients, API layer, services, data and cloud.
- A new "Selected architecture work" section covers the five resume case studies with their results (30% lower start-up latency, 40% faster incident resolution, releases in 2 hours instead of 2 days, 4x deployment frequency).
- Services, skills and SEO keywords now include Node.js, REST, GraphQL, WebSockets, microservices, databases, AWS and Azure.
- Experience matches the resume: Android Developer at Abbacus, the two freelance periods, and I2IT Pune.
- The app list is unchanged from version 1.

---


Plain HTML and CSS with no framework and no build step. A tiny inline script runs the "Copy email" button. Everything is in one page, so there's one request for HTML, one for fonts, and nothing else.

## Files
| File | Purpose |
|---|---|
| index.html | The whole site, with inline CSS, meta tags, Open Graph and JSON-LD (Person + ProfilePage) |
| 404.html | Not-found page (noindex) |
| robots.txt, sitemap.xml | Crawl rules and sitemap |
| og-image.png | 1200x630 preview for LinkedIn, WhatsApp and X |
| favicon.svg, favicon-32.png, apple-touch-icon.png, icon-512.png, site.webmanifest | Icons |
| _headers | Security and cache headers (Cloudflare Pages / Netlify format) |
| _redirects | Sends old /projects links to /#apps with a 301 |

## Before you go live
1. **Add your CV** as `keyur-mehta-cv.pdf` in this folder. Both "Download CV" buttons point to it. Export it only after making the resume edits below, so the site and CV say the same thing.
2. **Run the link checker:** `python3 check-links.py`. It tests every external link and lists any that are gone. Remove or fix those apps, then run it again.
3. **Resume edits that keep the CV in line with the site:**
   - "12+ years in solution and platform architecture" becomes "8+ years in solution and platform architecture". Also split the Brainvire entry so the title before your architect promotion is shown with its own dates.
   - "Led cross-functional teams of 50+ engineers" becomes "Technical lead and mentor to 50+ engineers across architecture, backend, QA and DevOps".
   - The header link `keyurmehta.in/projects` becomes `keyurmehta.in`.
4. Optional: swap `og-image.png` for a version with your photo.

## Deploy (Cloudflare Pages, free, recommended)
1. Push this folder to a GitHub repo, or use "Upload assets" in Cloudflare Pages.
2. Build command: none. Output directory: `/`.
3. Custom domains: add `keyurmehta.in` and `www.keyurmehta.in`. Move the domain's DNS to Cloudflare, or add the CNAME it shows you at your registrar.
4. Redirect `www` to the apex domain (Rules, then Redirect Rules) so there's one canonical URL.
5. Cancel the Weblium plan only after the new site is live and serving HTTPS.

Netlify works the same way, and it reads `_headers` and `_redirects` too. On GitHub Pages those two files are ignored. The site still works there, but you lose the security headers and the /projects redirect.

## After launch
- Google Search Console: verify the domain, submit `https://keyurmehta.in/sitemap.xml`, then request indexing for the home page.
- Test with PageSpeed Insights, the Rich Results Test (Person markup) and the LinkedIn Post Inspector, which refreshes the cached preview.
- When you change content, update `dateModified` in the JSON-LD and `lastmod` in sitemap.xml.

## What changed from the old site
**Accuracy fixes**
- IIFL MyMoney's Google Play link pointed to the XSEED app, and its App Store link was `#`. It's now marked "No longer listed". Add real links if it's still live.
- Puma Pris Africa's App Store link pointed to the Ontime app. I removed it and kept the Play link.
- TawasolMap's App Store URL had stray text (" TawasolMap") that broke it.
- Typos fixed: "Insomanic" to Insomnia, "Enginner" to Engineer, "BACHELOR OF Engineer" to B.E.
- The email address was scrambled (`moc.liamg%404002athemsk`) in the hero and contact sections, so it showed backwards. Now it's a working mailto with a copy button.
- Removed leftover template text ("courses on marketing and creative writing") and the uneven skill levels (Senior, Middle, Medium).
- Changed the "Technical Manager" tagline to wording that matches your real scope: hiring, mentoring and architecture ownership.

**SEO**
- Descriptive title and meta description. The old ones said only "Keyur Mehta's Portfolio".
- One H1 (your name), a clean heading hierarchy and semantic landmarks.
- JSON-LD Person schema: job title, employer, education, skills, LinkedIn and GitHub.
- Full Open Graph and Twitter tags with a real preview image.
- Projects merged into the home page, so all content sits on one indexed URL. Old /projects links redirect.

**Speed**
- No site builder runtime and no images apart from a 46 KB OG image that visitors never download. The page is about 41 KB of HTML before compression.
- Fonts are preconnected and use `display=swap`, so text shows immediately.

**Accessibility and responsiveness**
- Skip link, visible keyboard focus, reduced-motion support, text descriptions on the diagram, and AA contrast in light and dark mode.
- Checked at 390px with no horizontal scroll.
