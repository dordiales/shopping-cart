var app = Vue.createApp({
  data() {
    return {
      userName: "Joseph",

      items: [],

      discount: { value: -3.0, apply: false },

      productToInsert: "",

      unitToInsert: "",

      priceunitToInsert: "",
    };
  },
  computed: {
    subTotalBox() {
      let totalValue = 0.0;
      for (item of this.filteredItems) {
        let subTotalCalc = this.subTotal(item);
        totalValue = totalValue + subTotalCalc;
      }
      return totalValue;
    },

    totalBox() {
      if (this.discount.apply == true) {
        return this.subTotalBox + this.discount.value;
      } else {
        return this.subTotalBox;
      }
    },

    countProduct() {
      itemsCount = 0;
      for (item of this.filteredItems) {
        itemsCount += 1;
      }
      return itemsCount;
    },

    filteredItems() {
      let filtered = [];
      for (item of this.items) {
        if (!item.deleted) {
          filtered.push(item);
        }
      }
      return filtered;
    },
  },
  mounted() {
    this.loadProducts();
  },
  methods: {
    subTotal(data) {
      let cuantity = data["cuantity"];
      let value = data["value"];
      let result = cuantity * value;
      return result;
    },
    hideRow(task) {
      task.deleted = true;
    },
    async loadProducts() {
      let response = await fetch("http://192.168.21.143:5000/shopping-cart");
      this.items = await response.json();
    },
    async insertProduct() {
      let subTotalToInsert = this.unitToInsert * this.priceunitToInsert;
      let productToSend = {
        product: this.productToInsert,
        cuantity: this.unitToInsert,
        subtotal: subTotalToInsert,
        value: this.priceunitToInsert,
      };
      const settings = {
        method: "POST",
        body: JSON.stringify(productToSend),
        headers: {
          'Content-Type': 'application/json'
      }
      };
      let response = await fetch(
        "http://192.168.21.143:5000/shopping-cart", settings)
      this.items.push(productToSend)
    },
  },
});
app.mount("#app");
