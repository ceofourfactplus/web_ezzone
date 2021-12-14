<template>
  <li class="nav-item dropdown">
    <a
      class="nav-link d-flex dropdown-toggle"
      href="#"
      id="navbarDropdown"
      role="button"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      {{ $store.state.auth.userInfo.first_name }}
    </a>
    <ul
      class="dropdown-menu dropdown-menu-dark"
      aria-labelledby="navbarDropdown"
    >
      <li class="dropdown-item" v-if="$store.state.auth.accessToken != null">
        <router-link class="nav-link fw-bold" :to="{ name: 'Logout' }"
          >Log out</router-link
        >
      </li>
    </ul>
  </li>
</template>

<script>
export default {};
</script>

<style>
</style>