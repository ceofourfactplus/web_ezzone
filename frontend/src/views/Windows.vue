<template>
  <div class="container" id="windows">
    <div class="position-absolute top-50 start-50 translate-middle row">
      <div class="col">
        <div class="card">
          <img src="../assets/warehouse.jpeg" class="card-img-top" />
          <div class="card-body" style="height: 350px; overflow:auto;">
            <h5 class="card-title">Stock</h5>
            <div class="container card-text">
              <hr />
              <p>use to see all stock or create invoice and pick up</p>
              <hr />
              <p>Stock</p>
              <hr />
              <p>Invoice</p>
              <hr />
              <p>Pick Up</p>
              <hr />
              <p>To Buy</p>
              <hr />
              <p></p>
            </div>
          </div>
          <div class="card-footer">
            <router-link
              class="btn btn-danger"
              :to="{ path: '/all-stock' }"
            >
              GO to Stock Page
            </router-link>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card" >
          <img src="../assets/counter.jpeg" class="card-img-top" />
          <div class="card-body" style="height: 350px">
            <h5 class="card-title">POS</h5>
            <div class="card-text container">
              <hr />
              <p>use to create order for customer have:</p>
              <hr />
              <p>Topping</p>
              <hr />
              <p>Category</p>
              <hr />
              <p>Product</p>
              <hr />
              <p>Bill</p>
            </div>
            

          </div>
          <div class="card-footer">
                        <router-link class="btn btn-danger" :to="{ name: 'POS' }">
              GO to POS page
            </router-link>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card">
          <img src="../assets/production.jpeg" class="card-img-top" />
          <div class="card-body" style="height: 350px">
            <h5 class="card-title">PRODUCT</h5>
            <div class="card-text container">
              <hr />
              <p>use to create/edit product for admin have:</p>
              <hr />
              <p>Topping</p>
              <hr />
              <p>Category</p>
              <hr />
              <p>Product</p>
              <hr />
            </div>
          </div>
          <div class="card-footer">
            <router-link class="btn btn-danger" :to="{name:'SelectApp'}">
              GO to Product page
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Windows",
  methos:{
    ToProduct(){
      this.router.push("/products")
    }
  }
};
</script>
