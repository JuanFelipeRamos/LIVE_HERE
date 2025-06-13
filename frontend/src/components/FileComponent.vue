<template>
  <label for="File" class="upload-label">
    <div class="upload-content">
      <span class="upload-text">Sube tu foto</span>

      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="upload-icon"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M7.5 7.5h-.75A2.25 2.25 0 0 0 4.5 9.75v7.5a2.25 2.25 0 0 0 2.25 2.25h7.5a2.25 2.25 0 0 0 2.25-2.25v-7.5a2.25 2.25 0 0 0-2.25-2.25h-.75m0-3-3-3m0 0-3 3m3-3v11.25m6-2.25h.75a2.25 2.25 0 0 1 2.25 2.25v7.5a2.25 2.25 0 0 1-2.25 2.25h-7.5a2.25 2.25 0 0 1-2.25-2.25v-.75"
        />
      </svg>
    </div>

    <input multiple type="file" id="File" class="file-input" />
  </label>
</template>

<style scoped>
label {
  cursor: pointer;
}

.upload-label {
  display: block;
  max-width: 400px; /* límite de ancho */
  margin: 0 auto;
  border-radius: 0.5rem;
  border: 1px solid #d1d5db;
  padding: 1rem;
  color: #111827;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.upload-label:hover {
  border-color: #9798ac;
}

@media (min-width: 640px) {
  .upload-label {
    padding: 1.5rem;
  }
}

.upload-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.upload-text {
  font-weight: 500;
}

.upload-icon {
  width: 1.5rem;
  height: 1.5rem;
}

.file-input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>
