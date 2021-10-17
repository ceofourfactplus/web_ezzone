<template>
  <div id="list-category">
    <table class="table table-dark">
      <thead>
        <tr>
          <th>#</th>
          <th>Category</th>
          <th>able</th>
          <th>edit/delete</th>
        </tr>
      </thead>
      <tbody class="scroll">
        <tr v-for="(category, index) in categories" :key="category.id">
          <td>{{ index + 1 }}</td>
          <td>{{ category.category }}</td>
          <td>
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                :value="category.status"
                id="flexSwitchCheckDefault"
              />
            </div>
          </td>
          <td>
            <button class="btn btn-warning"><i class="fas fa-arrow-alt-circle-up"></i>update</button>
						<button class="btn btn-danger"><i class="fas fa-trash-alt"></i>delete</button>
          </td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
export default {
	name:"Category",  
	data(){
		return{
			categories:[]
		}
	}
};
</script>

<style>
.scroll{
	scroll-behavior: smooth;
}
</style>