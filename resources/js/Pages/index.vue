<script setup lang="ts">
import { Link, Head, useForm } from "@inertiajs/vue3";

import Button from "primevue/button";
import InputText from "primevue/inputtext";
import 'primevue/resources/themes/lara-light-purple/theme.css'
import { reactive } from "vue";

const form = useForm({
  name: "",
})

</script>


<template>
  <Head>
    <title>Form</title>
  </Head>
  <form @submit.prevent="form.post('/', {
    method: 'post',
    onSuccess: () => console.log('done'),
    preserveScroll: true,
  })">
    <div class="center">
      <div class="space-y-3">
        <label for="username">Username</label>
        <InputText id="username" name="username" placeholder="Username" v-model="form.name" />
        <Button type="submit">Submit</Button>
      </div>
    </div>
  </form>
</template>

<style scoped>
label {
  display: block;
}
input {
  display: block;
}
button {
  display: block;
}

.center {
  display: flex;
  justify-content: center;
}
.center div {
  gap: 0.5rem;
}
</style>
