<script setup></script>

<template>
  <div class = "container">

   <h1>AI Business Requirements Assistant</h1>

   <p> 
    Describe your business idea below.
   </p>

   <textarea
   placeholder = "Describe your business idea below.">
   </textarea>

   <button> Analyze </button>
</div>
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
}

button{
  padding: 12px;
  font-size: 16px;
  cursor: pointer;
}

</style>
