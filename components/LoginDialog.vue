<template>
  <div>
    <v-form @submit="onLoginSubmit">
      <v-text-field v-model="username" placeholder="Username" />
      <v-text-field v-password="password" placeholder="Password" type="password" />
    </v-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async onLoginSubmit () {
      data = {
        username: this.username,
        password: this.password
      }
      try {
        let resp = await this.$auth.loginWith('local', { data })
      } catch (err) {
        console.log(err)
      }
  }
}
</script>
