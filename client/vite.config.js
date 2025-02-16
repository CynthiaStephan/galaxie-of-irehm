import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,  // Définir le bon port
    host: '0.0.0.0',  // Permettre l'accès depuis d'autres conteneurs Docker
  },
})
