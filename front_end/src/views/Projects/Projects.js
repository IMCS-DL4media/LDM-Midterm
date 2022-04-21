import { mymixin } from '../../mixins/mixins.js'

console.log("in projects")

// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
// import router from "../../router.js";

import Vue from "vue";
import VueResource from 'vue-resource';
Vue.use(VueResource);

export default {
	name: "Projects",
	data: {
		showModal: false,
	},
	props: ['user_id'],
	components: {},
	mixins:[mymixin],
	methods: {
		// createNewProjectClicked() {
			// console.log("in create new project", $("#myModal").length)

			// $("#myModal").modal("show");


			// var user_id_prm;
			// if (this.user_id == undefined) {
			//   //default user id
			//   user_id_prm = "1"
			// } else{
			//   user_id_prm = this.user_id
			// }
			// router.push("/addproject/" + user_id_prm )
		// }
		createNewProjectClicked:function(e) {
			// console.log("in create new project", $("#myModal").length)
			// console.log($("#project_name_id").value);
			// console.log($("#training_file_input_id").value);
			// console.log($("#training_file_input").value);

			//e.preventDefault();

			// console.log( document.getElementById("project_name_id").value)
			// console.log( document.getElementById("training_file_input_id").value)
			
			// console.log(this.$refs);
			// console.log(this.$refs.fileInputRef);

			$('#alerts_success').hide();
			$('#alerts_fail').hide();

			let fileToUpload = this.$refs.fileInputRef.files[0];
			  
			let formData = new FormData();
			
			formData.append('project_name', document.getElementById("project_name_id").value);			  
			formData.append('zip_file', fileToUpload);
			
			
			// console.log(formData);
			// for (var key of formData.entries()) {
			// 	console.log(key[0] + ', ' + key[1]);
			// }

			this.$http.post(  this.SERVER_URL() + "create_new_project", formData)
				.then(response => {					
					console.log(response.body)				
					$('#alerts_success').show();
				},
				response => {						
					console.log(response.body)				
					$('#alerts_fail').show();
				})
			
			return;

			// var user_id_prm;
			// if (this.user_id == undefined) {
			//   //default user id
			//   user_id_prm = "1"
			// } else{
			//   user_id_prm = this.user_id
			// }
			// router.push("/addproject/" + user_id_prm )
		}		
	}
};
