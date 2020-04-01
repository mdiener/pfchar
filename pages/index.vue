<template>
  <div id="page">
    <div v-if="user.loggedin">
      <LoginDialog />
    </div>
    <div v-else>
      <CharacterSelection />
    </div>
  </div>
</template>

<script>
import LoginDialog from '~/components/LoginDialog'
import CharacterSelection from '~/components/CharacterSelection'

export default {
  layout: 'default',
  components: {
    LoginDialog,
    CharacterSelection
  },
  computed: {
    user () {
      return this.$store.user
    }
  }
}
</script>

<style scoped>

</style>
