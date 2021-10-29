<template>
<div>
  <nav
    class="
      navbar navbar-expand-lg navbar-dark
      bg-dark
      border-bottom border-light
    "
  >
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'Home' }"
        >EZ zone</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 fs-6">
          <!-- create -->
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle fw-bold"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Create
            </a>
            <ul
              class="dropdown-menu dropdown-menu-dark"
              aria-labelledby="navbarDropdown"
            >
              <!-- create invoice -->
              <li class="dropdown-item">
                <a
                  type="button"
                  href="#"
                  class="nav-link fw-bold"
                  data-bs-toggle="modal"
                  data-bs-target="#add-invoice"
                >
                  Create Invoice
                </a>
              </li>
              <!-- create supplier -->
              <li class="dropdown-item">
                <a
                  type="button"
                  class="nav-link fw-bold"
                  data-bs-toggle="modal"
                  data-bs-target="#add-supplier"
                >
                  Create Supplier
                </a>
              </li>
              <!-- creaet stock -->
              <li class="dropdown-item">
                <a
                  type="button"
                  class="nav-link fw-bold"
                  data-bs-toggle="modal"
                  data-bs-target="#create-stock"
                >
                  Create Stock
                </a>
              </li>
              <!-- create payer -->
              <li class="dropdown-item">
                <a
                  type="button"
                  class="nav-link fw-bold"
                  data-bs-toggle="modal"
                  data-bs-target="#payer"
                >
                  Create Payer
                </a>
              </li>
              <!-- create unit -->
              <li class="dropdown-item">
                <a
                  type="button"
                  class="nav-link fw-bold"
                  data-bs-toggle="modal"
                  data-bs-target="#unit-modal"
                >
                  Create Unit
                </a>
              </li>
            </ul>
          </li>
          <!-- to buy -->
          <li class="nav-item">
            <a
              type="button"
              class="nav-link fw-bold"
              data-bs-toggle="modal"
              data-bs-target="#to-buy"
            >
              To Buy
            </a>
          </li>
          <!-- pick up -->
          <li class="nav-item">
            <a
              type="button"
              class="nav-link fw-bold"
              data-bs-toggle="modal"
              data-bs-target="#pick-up"
            >
              Pick Up
            </a>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <form class="d-flex">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
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
        </ul>
      </div>
    </div>
  </nav>
  <modal-invoice />
    <modal-inventory />
    <modal-supplier />
    <modal-payer />
    <unit-modal />
</div>
  
</template>

<script>
import ModalInvoice from "./InvoiceModal.vue";
import ModalInventory from "./StockModal.vue";
import ModalSupplier from "./SupplierModal.vue";
import ModalPayer from "./PayerModal.vue";
import UnitModal from "./UnitModal.vue";
import {mapState} from 'vuex'
export default {
  name: "NavbarStock",
  computed: mapState(["auth"]),
  components: {
    ModalInvoice,
    ModalInventory,
    ModalSupplier,
    ModalPayer,
    UnitModal,
  },
};
</script>
