// import axios from 'axios';

export default {
  state:{
    category:[],
    select_app:'',
    side_nav: [
      {img: require('../../assets/icon/nav-product.png'), name: 'Product', url_name: 'Product', style: "margin-left: -20px;",},
      {img: require('../../assets/icon/nav-category.png'), name: 'Category P.', url_name: 'ProductCategory', style: "margin-left: -20px;",},
      {img: require('../../assets/icon/tropping-orange.png'), name: 'Topping', url_name: 'Topping', style: "margin-left: -20px;",},
      {img: require('../../assets/icon/nav-category.png'), name: 'Category T.', url_name: 'ToppingCategory', style: "margin-left: -20px;",},
  ],
    active_page:'',
  }
}