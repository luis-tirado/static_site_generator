# Static Site Generator

A lightweight, Python-powered static site generator (SSG) designed to transform Markdown content into a structured, styled web experience using a central HTML template.

## 🚀 Features

* **Markdown Support:** Easily write content in Markdown and have it converted to HTML.
* **Template Driven:** Maintain a consistent look and feel across your entire site using `template.html`.
* **Asset Management:** Automatically handles static assets like CSS and images.
* **Automated Builds:** Simple shell scripts to handle the build and testing process.

## 📁 Project Structure

```text
.
├── content/        # Your raw Markdown (.md) source files
├── docs/           # The final output directory (ready for deployment)
├── src/            # Core Python logic for the generator
├── static/         # Static assets (CSS, images, etc.)
├── build.sh        # Script to build the project
├── main.sh         # Entry point for the application
├── test.sh         # Script to run project tests
└── template.html   # The base HTML layout for all pages
