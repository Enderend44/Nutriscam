/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Poppins"],
        title: ["Dancing Script"],
      },
      colors: {
        "default": "#282C2B"
      },
    }
  },
  plugins: [],
}