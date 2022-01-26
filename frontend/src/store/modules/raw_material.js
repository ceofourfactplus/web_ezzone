export default {
    state:{
        page: null,
        tab: "All",
        status_image: {
            1: {img: require('../../assets/icon/correct.png'), txt: 'In Stock', class: 'btn-g', style: 'width: 50px; height: 50px;transform:rotate(180deg);'} ,
            2: {img: require('../../assets/icon/warning.png'), txt: 'Minimum', class: 'btn-y', style: 'width: 50px; height: 50px;'} ,
            3: {img: require('../../assets/icon/incorrect.png'), txt: 'Out of Stock', class: 'btn-r', style: 'width: 50px; height: 50px;'} ,
        },
        side_nav: [
            {img: require('../../assets/icon/RM-mini.png'), name: 'Raw Materials', url_name: 'RawMaterials', style: "margin-left: -20px;",},
            {img: require('../../assets/icon/po-notice-30x40.png'), name: 'PO Notice', url_name: 'PONotice', style: "margin-left: -20px;",},
            {img: require('../../assets/icon/po-30x40.png'), name: 'Purchase Order', url_name: 'PO', style: "margin-left: -35px;", img_style: "width: 55px; height: 60px;",},
            {img: require('../../assets/icon/pickup-rm-30x40.png'), name: 'Pickup List', url_name: 'PickupList', style: "margin-left: -35px;", img_style: "width: 55px; height: 60px;",},
            {img: require('../../assets/icon/category-30x40.png'), name: 'Category', url_name: 'RawMaterialCategory', style: "margin-left: -20px;",},
        ],
        all_receipt: [],
        all_receipt_detail: [],
        all_po_selected: [],
    }
  }