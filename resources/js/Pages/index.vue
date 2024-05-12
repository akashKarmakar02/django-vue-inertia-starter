<script setup lang="ts">
import { Link, Head, useForm } from "@inertiajs/vue3";
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
    preserveScroll: true,
  })">
    <div class="flex justify-center">
      <div class="space-y-3">
        <label for="username">Username</label>
        <button>Hello</button>
      </div>
    </div>
  </form>
</template>
