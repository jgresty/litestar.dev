copyright = "2023 - The Litestar Organization"  # noqa: A001

html_theme = "litestar_sphinx_theme"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

templates_path = ["_templates"]

html_static_path = ["_static"]
html_show_sourcelink = False
html_sidebars = {"**": []}
html_additional_pages = {"index": "landing-page.html"}
nitpicky = True

html_theme_options = {
    "use_page_nav": False,
    "show_prev_next": False,
    "github_repo_name": "litestar",
    "extra_navbar_items": {
        "Docs": "https://docs.litestar.dev",
        "Community": {
            "Contributing": {
                "description": "Learn how to contribute to the Litestar project",
                "link": "/contributing",
                "icon": "contributing",
            },
            "Code of Conduct": {
                "description": "Review the etiquette for interacting with the Litestar community",
                "link": "/code-of-conduct",
                "icon": "coc",
            },
        },
        "About": {
            "Litestar Organization": {
                "description": "Details about the Litestar organization",
                "link": "about/organization",
                "icon": "org",
            },
            "Releases": {
                "description": "View the release history for Litestar",
                "link": "about/litestar-releases",
                "icon": "releases",
            },
        },
        "Help": "https://github.com/orgs/litestar-org/discussions",
    },
}

html_context = {
    "code_sample": True,
    "info_cards": [
        {
            "title": "Fully-featured",
            "content": (
                "Everything that's needed to build modern APIs, from data serialization and validation to websockets, "
                "ORM integration, session management, authentication and more"
            ),
            "icon": None,
            "link": None,
        },
        {
            "title": "Fast",
            "content": (
                "Starlite puts great emphasis on developer experience and performance: It's one of the fastest "
                "ASGI frameworks and developing with it is just as fast"
            ),
            "icon": None,
            "link": "https://docs.litestar.dev/latest/benchmarks",
        },
        {
            "title": "(a)synchronous",
            "content": (
                "Asynchronous at heart, but with synchronous execution not as a second class citizen: "
                "Synchronous applications run without performance penalties"
            ),
            "icon": None,
            "link": None,
        },
    ],
    "feature_cards": [
        {
            "title": "Data Validation And Parsing",
            "content": "Leverage power of type hints to define how data should be validated, parsed and serialized",
            "link": "https://docs.litestar.dev/2/usage/dto.html",
        },
        {
            "title": "Open Ecosystem",
            "content": (
                "Define schemas and models for validation with standard types such as dataclasses, libraries like "
                "Pydantic, or integrate your own"
            ),
        },
        {
            "title": "OpenAPI",
            "content": (
                "Automatically generated OpenAPI schemas help to document APIs and integrate with the frontend via "
                "TypeScript schema generation"
            ),
            "link": "https://docs.litestar.dev/2/usage/openapi.html",
        },
        {
            "title": "Interactive API documentation",
            "content": (
                "Interactively explore your APIs through Swagger, Redoc or Stoplight Elements, powered by OpenAPI"
            ),
        },
        {
            "title": "Middlewares",
            "content": (
                "Handle rate-limiting, CORS, CSRF, compression, logging and many more common tasks with Litestar's "
                "built-in middlewares"
            ),
            "link": "https://docs.litestar.dev/2/usage/middleware/builtin-middleware.html",
        },
        {
            "title": "Data Stores",
            "content": (
                "Interfaces for various key/value stores that seamlessly integrate with "
                "your application and third party extensions"
            ),
            "link": "https://docs.litestar.dev/2/usage/stores.html",
        },
        {
            "title": "ORM Integration",
            "content": (
                "First-class SQLAlchemy support let's you use your models for validation and serialization directly,"
                " reducing code duplication"
            ),
            "link": "https://docs.litestar.dev/2/usage/plugins/sqlalchemy.html",
        },
        {
            "title": "Dependency Injection",
            "content": (
                "Powerful dependency injection on all application layers, aides in code decoupling and reduces "
                "repetition"
            ),
            "link": "https://docs.litestar.dev/2/usage/dependency-injection.html",
        },
        {
            "title": "Caching",
            "content": "Response caching with minimal configuration and overhead to speed up response times",
            "link": "https://docs.litestar.dev/2/usage/caching.html",
        },
        {
            "title": "WebSockets",
            "content": (
                "Easy to used WebSockets integration, featuring high and low-level APIs and support for automatic data "
                "validation and serialization"
            ),
            "link": "https://docs.litestar.dev/2/usage/websockets.html",
        },
        {
            "title": "Runtime safety through strict validation",
            "content": (
                "Litestar is strictly typed, and user supplied functions are meticulously validated to minimize "
                "runtime errors"
            ),
            "link": "https://docs.litestar.dev/2/usage/route-handlers.html",
        },
        {
            "title": "Authentication And Authorization",
            "content": (
                "Session and JWT based authentication and utilities at your disposal to start building your "
                "authentication layer"
            ),
            "link": "https://docs.litestar.dev/2/usage/security.html",
        },
    ],
    "announcement": {
        "title": "Litestar 2.0.0alpha3 is available",
        "description": "Check out the latest release here",
        "link": "https://github.com/litestar-org/litestar/releases/tag/v2.0.0alpha3",
    },
    "project_name": "Litestar",
    "project_url": "https://litestar.dev",
    "project_github_url": "https://github.com/litestar-org/litestar",
    "project_tagline": "Effortlessly build performant APIs",
    "project_description_short": "The powerful, lightweight and flexible ASGI framework",
}
