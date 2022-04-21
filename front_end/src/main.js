import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// import BootstrapVue from 'bootstrap-vue'



let jQuery = require('jquery');

global.$ = jQuery;



// let bootstrap = require('bootstrap-vue');


// import BootstrapVue from 'bootstrap-vue'

import 'bootstrap';

// Vue.use(BootstrapVue);



Vue.config.productionTip = false;
// Vue.use(BootstrapVue);

// Vue.use(jQuery);



//export const SERVER_URL_CONST = "localhost:5000";
//back_end is docker container name 
//export const SERVER_URL_CONST = "back_end:5000";


new Vue({
  router,
  store,
  data: {
		currentUser : 1,
		projects : []
  },

  created(){
		//console.log( process );
		//console.log( process.env );
		//console.log( process.env.VUE_APP_SERVER_URL );
  		//console.log("in created this", this)


		fetch( 'http://' + process.env.VUE_APP_SERVER_URL + '/get_projects?user=1')
		.then(response=>response.json())
		.then(json => {

			console.log("in json ", json)

			this.projects = json.projects
	  })	  
	},
  render: h => h(App)
}).$mount("#app");
