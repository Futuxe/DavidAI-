import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
  build: {
    outDir: 'dist',
  },
  define: {
    // jeśli chcesz używać zmiennej środowiskowej w kodzie, np. VITE_API_URL
    'process.env': {}
  }
});
