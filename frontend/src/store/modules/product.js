// import axios from 'axios';

export default {
  state:{
    category:[],
    select_app:'',
    side_nav: [
      {img: require('../../assets/icon/nav-product.png'), name: 'Product', url_name: 'Product', style: "margin-left: -20px;",},
      {img: require('../../assets/icon/nav-category.png'), name: 'Category', url_name: 'ProductCategory', style: "margin-left: -20px;",},
  ],
    active_page:'',
  }
}