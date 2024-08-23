module.exports = {
  mode: 'jit',
  content: ['./app/templates/**/*.html'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        'jakarta': ['Plus Jakarta', 'sans-serif'],
        'plex-mono': ['IBM Plex Mono', 'monospace'],
      },
      "colors": {
        "site": "#13111C",
        "panel": "#1C1A28",
        "highlighted": "#33323E",
        "theme": {
          1: "#FF5001",
          2: "#A9F00F",
        }
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
