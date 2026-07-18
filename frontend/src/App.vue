<script setup>
import { computed, onMounted, ref } from 'vue'

const internshipGoal = ref('')
const planGenerated = ref(false)
const errorMessage = ref('')
const isLoading = ref(false)
const analysesHistory = ref([])
const isHistoryLoading = ref(false)
const historyError = ref('')

const maxCharacters = 2000

const characterCount = computed(() => internshipGoal.value.length)

const preparationSections = [
  {
    key: 'required_skills',
    title: 'Required Skills',
    description: 'Technical and soft skills required for the internship',
    icon: '✅',
    emptyText: 'No skills identified yet',
  },

  {
    key: 'learning_plan',
    title: 'Learning Plan',
    description: 'Recommended topics and learning order',
    icon: '📚',
    emptyText: 'No learning plan generated yet',
  },

  {
    key: 'skill_gaps',
    title: 'Skill Gaps',
    description: 'Knowledge and experience you still need',
    icon: '⬆️',
    emptyText: 'No skill gaps identified yet',
  },

  {
    key: 'next_steps',
    title: 'Next Steps',
    description: 'Recommended actions to move forward',
    icon: '🚩',
    emptyText: 'No next steps generated yet',
  },
]

const results = ref({
  required_skills: [],
  learning_plan: [],
  skill_gaps: [],
  next_steps: [],
})

const isGeneratedDisabled = computed(() => {
  return internshipGoal.value.trim().length === 0 || isLoading.value
})

function clearForm() {
  internshipGoal.value = ''
  errorMessage.value = ''

  results.value = {
    required_skills: [],
    learning_plan: [],
    skill_gaps: [],
    next_steps: [],
  }
}

async function analyzeIdea() {
  errorMessage.value = ''

  if (!internshipGoal.value.trim()) {
    errorMessage.value = 'Please describe your internship goal.'
    return
  }

  isLoading.value = true

  try {
    const response = await fetch('http://127.0.0.1:8000/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        internship_goal: internshipGoal.value,
      }),
    })

    if (!response.ok) {
      throw new Error('The backend could not generate the learning plan.')
    }

    const data = await response.json()

    results.value = {
      required_skills: data.required_skills || [],
      learning_plan: data.learning_plan || [],
      skill_gaps: data.skill_gaps || [],
      next_steps: data.next_steps || [],
    }

    planGenerated.value = true
    await loadHistory()
  } catch (error) {
    console.error(error)
    errorMessage.value = 'The learning plan could not be generated. Please try again.'
  } finally {
    isLoading.value = false
  }
}

async function loadHistory() {
  historyError.value = ''
  isHistoryLoading.value = true

  try {
    const response = await fetch('http://127.0.0.1:8000/analyses')

    if (!response.ok) {
      throw new Error('Could not load history.')
    }

    const data = await response.json()
    analysesHistory.value = Array.isArray(data) ? data : []
  } catch (error) {
    console.error(error)
    historyError.value = 'Could not load your previous analyses.'
    analysesHistory.value = []
  } finally {
    isHistoryLoading.value = false
  }
}

function openAnalysis(analysis) {
  internshipGoal.value = analysis.internship_goal

  results.value = {
    required_skills: analysis.required_skills,
    learning_plan: analysis.learning_plan,
    skill_gaps: analysis.skill_gaps,
    next_steps: analysis.next_steps,
  }

  planGenerated.value = true
  errorMessage.value = ''

  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  })
}

onMounted(() => {
  loadHistory()
})
</script>

<template>
  <main class="page">
    <section class="intro">
      <p class="eyebrow">AI-powered internship preparation</p>

      <h1>AI Internship Preparation Assistant</h1>

      <p class="subtitle">
        Analyze your current skills, see where you can do better and receive a personalized learning
        plan for your dream internship.
      </p>
    </section>

    <section class="input-card">
      <div class="input-header">
        <div>
          <h2>Describe your internship goal</h2>

          <p>Include the position you want and the skills you already have.</p>
        </div>

        <span> {{ characterCount }} / {{ maxCharacters }} </span>
      </div>

      <textarea
        v-model="internshipGoal"
        :maxlength="maxCharacters"
        placeholder="Example: I want to become a Backend Developer. I already know Python and SQL, but I have no experience with REST APIs or Docker."
      ></textarea>

      <p v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </p>

      <div class="actions">
        <button type="button" class="secondary-button" @click="clearForm">Clear</button>

        <button
          type="button"
          class="primary-button"
          :disabled="isGeneratedDisabled"
          @click="analyzeIdea"
        >
          {{ isLoading ? 'Generating...' : 'Generate Learning Plan' }}
        </button>
      </div>
    </section>

    <section v-if="planGenerated" class="results-section">
      <div class="results-header">
        <div>
          <h2>Preparation Results</h2>
          <p>AI-generated skills and recommendations for your internship goal.</p>
        </div>
      </div>

      <div class="results-grid">
        <article v-for="section in preparationSections" :key="section.key" class="result-card">
          <div class="result-card-header">
            <div class="result-icon">
              {{ section.icon }}
            </div>

            <div>
              <h3>{{ section.title }}</h3>
              <p>{{ section.description }}</p>
            </div>

            <span class="result-count">
              {{ results[section.key].length }}
            </span>
          </div>

          <ul v-if="results[section.key].length > 0" class="result-list">
            <li v-for="item in results[section.key]" :key="item">
              {{ item }}
            </li>
          </ul>

          <div v-else class="empty-state">
            <div class="empty-icon">
              {{ section.icon }}
            </div>

            <p>{{ section.emptyText }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="history-section">
      <div class="history-header">
        <div>
          <h2>Previous Analyses</h2>
          <p>Open a previously generated internship preparation plan.</p>
        </div>

        <button
          type="button"
          class="secondary-button history-refresh-button"
          :disabled="isHistoryLoading"
          @click="loadHistory"
        >
          {{ isHistoryLoading ? 'Loading...' : 'Refresh History' }}
        </button>
      </div>

      <p v-if="historyError" class="error-message">
        {{ historyError }}
      </p>

      <p v-else-if="!isHistoryLoading && analysesHistory.length === 0" class="empty-history">
        No saved analyses yet.
      </p>

      <div v-else class="history-list">
        <button
          v-for="analysis in analysesHistory"
          :key="analysis.id"
          type="button"
          class="history-item"
          @click="openAnalysis(analysis)"
        >
          <span class="history-goal">
            {{ analysis.internship_goal }}
          </span>

          <span class="history-date">
            {{ new Date(analysis.created_at).toLocaleString() }}
          </span>
        </button>
      </div>
    </section>
  </main>
</template>

<style scoped>
.page {
  max-width: 1000px;
  margin: 0 auto;
  padding: 48px 24px;
}

.intro {
  margin-bottom: 32px;
}

.eyebrow {
  margin-bottom: 12px;
  color: #2563eb;
  font-size: 14px;
  font-weight: 600;
}

h1 {
  margin: 0;
  font-size: 40px;
  line-height: 1.2;
}

.subtitle {
  max-width: 720px;
  margin-top: 16px;
  color: #667085;
  font-size: 17px;
  line-height: 1.7;
}

.input-card {
  padding: 28px;
  border: 1px solid #e1e6ed;
  border-radius: 16px;
  background: white;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
}

.input-header {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 18px;
}

.input-header h2 {
  margin: 0;
}

.input-header p {
  margin: 8px 0 0;
  color: #667085;
}

textarea {
  width: 100%;
  min-height: 190px;
  padding: 16px;
  border: 1px solid #cfd7e3;
  border-radius: 12px;
  font-size: 16px;
  line-height: 1.6;
  resize: vertical;
}

textarea:focus {
  border-color: #2563eb;
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
}

.error-message {
  margin: 12px 0 0;
  color: #b42318;
}

.actions {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  gap: 16px;
  margin-top: 18px;
}

button {
  min-height: 48px;
  border: none;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.secondary-button {
  border: 1px solid #d5dce5;
  background: white;
  color: #111827;
}

.primary-button {
  background: #111827;
  color: white;
}

.primary-button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

.results-section {
  margin-top: 24px;
  padding: 28px;
  border: 1px solid #e1e6ed;
  border-radius: 16px;
  background: white;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
}

.results-header {
  margin-bottom: 22px;
}

.results-header h2 {
  margin: 0;
  font-size: 24px;
}

.results-header p {
  margin: 8px 0 0;
  color: #667085;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.result-card {
  padding: 18px;
  border: 1px solid #e1e6ed;
  border-radius: 14px;
  background: #ffffff;
}

.result-card-header {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: start;
  gap: 12px;
  margin-bottom: 14px;
}

.result-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: #f2f4f7;
  display: grid;
  place-items: center;
  font-size: 18px;
}

.result-card h3 {
  margin: 2px 0 4px;
  font-size: 16px;
}

.result-card-header p {
  margin: 0;
  color: #667085;
  font-size: 13px;
  line-height: 1.5;
}

.result-count {
  min-width: 28px;
  height: 28px;
  padding: 0 8px;
  border-radius: 999px;
  background: #f2f4f7;
  color: #667085;
  display: grid;
  place-items: center;
  font-size: 12px;
}

.empty-state {
  min-height: 130px;
  border: 1px solid #e4e7ec;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #7a8494;
  text-align: center;
}

.empty-icon {
  font-size: 28px;
  opacity: 0.75;
}

.empty-state p {
  margin: 0;
  font-size: 13px;
}

.result-list {
  margin: 0;
  padding-left: 22px;
  color: #344054;
  line-height: 1.7;
}

.history-section {
  margin-top: 24px;
  padding: 28px;
  border: 1px solid #e1e6ed;
  border-radius: 16px;
  background: white;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  margin-bottom: 22px;
}

.history-header h2 {
  margin: 0;
  font-size: 24px;
}

.history-header p {
  margin: 8px 0 0;
  color: #667085;
}

.history-refresh-button {
  padding: 0 18px;
  flex-shrink: 0;
}

.history-refresh-button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

.history-list {
  display: grid;
  gap: 12px;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  width: 100%;
  padding: 16px;
  border: 1px solid #e1e6ed;
  background: #f8fafc;
  text-align: left;
}

.history-item:hover {
  border-color: #98a2b3;
  background: #f2f4f7;
}

.history-goal {
  font-weight: 600;
  color: #111827;
}

.history-date {
  flex-shrink: 0;
  color: #667085;
  font-size: 13px;
}

.empty-history {
  margin: 0;
  color: #667085;
}

@media (max-width: 700px) {
  .page {
    padding: 28px 16px;
  }

  h1 {
    font-size: 32px;
  }

  .input-header {
    flex-direction: column;
  }

  .actions,
  .results-grid {
    grid-template-columns: 1fr;
  }

  .input-card,
  .results-section {
    padding: 20px;
  }

  .history-header,
  .history-item {
    flex-direction: column;
    align-items: stretch;
  }

  .history-section {
    padding: 20px;
  }
}
</style>
