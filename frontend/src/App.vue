<script setup>
import { ref } from "vue";

const businessIdea = ref("");
const result = ref("");
const errorMessage = ref("");

function analyzeIdea() {
  errorMessage.value = "";
  result.value = "";

  if(!businessIdea.value.trim()){
    errorMessage.value = "Please describe your business idea first.";
    return;
  }

  result.value = `Your idea "${businessIdea.value}" is ready for analysis.`; 
}
</script>

<template>
  <main class = "container">

   <h1>AI Business Requirements Assistant</h1>

   <p> 
    Describe your business idea below.
   </p>

   <textarea
   v-model = "businessIdea"
   placeholder = "Describe your business idea below.">
   </textarea>

   <button @click = "analyzeIdea"> Analyze </button>

   <p v-if="errorMessage" class="error">
   {{ errorMessage }}
   </p>

   <div v-if="result" class="result">
   <h2>Analysis result</h2>
   <p>{{ result }}</p>
   </div>

</main>
</template>

<style scoped>
.container{
  max-width: 800px;
  margin: 60px auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

textarea{
  min-height: 180px;
  padding: 15px;
  font-size: 16px;
  resize: vertical;
}

button{
  padding: 12px;
  font-size: 16px;
  cursor: pointer;
}

.error{
  color: crimson;
}

.result{
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

</style>
