<template>	
	<div>
		<TopBar></TopBar>

    <!-- 
      <ul >
        <li v-for="p in $parent.projects">{{p}}</li>
      </ul>
    -->
    
		<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">Create new project ...</button>
		<br/>
		<br/>
		<div id="alerts_fail"  class="alert alert-danger collapse" role="alert">
			Project creation failed.
			<button type="button" class="close" data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">&times;</span>
			</button>
		</div>
		
		<div id="alerts_success" class="alert alert-success collapse" role="alert">
			Project created successfully.
			<button type="button" class="close" data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">&times;</span>
			</button>
		</div>

		<form>
		
			<div class="form-check float-right">
				<input type="checkbox" class="form-check-input" id="showOnlyOwnedProjects" v-model= "showOnlyOwnedProjects">
				<label class="form-check-label" for="exampleCheck1">Show only owned projects</label>
			</div>
			<br/>
			<br/>
		</form>

		<!-- The Modal -->
		<div class="modal" id="myModal">
			<div class="modal-dialog">
				<div class="modal-content">

					<!-- Modal Header -->
					<div class="modal-header">
							<h4 class="modal-title">Create new project ... </h4>
							<button type="button" class="close" data-dismiss="modal">&times;</button>
					</div>

					<!-- Modal body -->
					<div class="modal-body">
						<div class="form-group">
							<label for="exampleInputEmail1">Project name:</label>
							<input type="text" class="form-control" id="project_name_id" aria-describedby="emailHelp" placeholder="Enter project name ... ">
							
						</div>

						<div class="form-group">
							<label for="exampleInputEmail1">Project type:</label>
							<select class="form-control" id = "project_type" disabled >
								<option value = "ImgClassification"> Image Classification</option>
								<option value = "ImgCaptioning"> Image Captioning</option>
							</select>
							
						</div>
										
						<div class="form-group">
							<label for="exampleInputEmail1">Project description:</label>
							<input type="text" class="form-control" id="project_description_id" aria-describedby="emailHelp" placeholder="Enter project description ... ">
							
						</div>

						<!-- 
						<div class="form-group" >
							<label for="exampleInputEmail1">Training data file:</label>
							<div class="file-loading">
								<input id="training_file_input_id" name="training_file_input" type="file" ref="fileInputRef" >
							</div>	
						</div> 
						-->
						
					</div>

					<!-- Modal footer -->
					<div class="modal-footer">
						<button type="button" class="btn btn-primary" data-dismiss="modal" @click="createNewProjectClicked">Create</button>
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
					</div>

				</div>
			</div>
		</div>

		<div class="row">
			<!-- {{projects}} -->
			<!-- Earnings (Monthly) Card Example -->
			<div class="col-xl-3 col-md-6 mb-4"  
					v-for="p in projects" :key="p.id" 
					v-if ="showOnlyOwnedProjects ? $store.getters.userId == p.owner_id : true">
				<div class="card border-left-primary shadow h-100 py-2">
					<div class="card-body">
						<div class="row no-gutters align-items-center">
							<div class="col mr-2">
							
								<router-link :to="'/project/' + p.id">
									<div class="h5 mb-0 font-weight-bold text-gray-800"> 
										Project name : {{ p.name }}
									</div>
								</router-link>

								<div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
									Project author : {{p.owner_id}}
								</div>
								<div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
									Last updated on : {{p.last_update_time}}
								</div>
								<div class="text-xs font-weight-bold text-primary text-uppercase mb-1"> 
									Num of runs : {{p.num_of_runs}}
								</div>
							
							</div>
							<!-- <div class="col-auto">
							<i class="fas fa-calendar fa-2x text-gray-300"></i>
							
							</div> -->
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	
</template>

<script src = "./ListOfProjects.js">

// export default {
//   name: 'app',
//   components: {
//     //VApp
//   },
//   data: function(){
//     return {
// 		  currentUser : 1,
//       projects : []
//     }
//   },
//   created(){
    
// 		//console.log( process );
// 		//console.log( process.env );
// 		//console.log( process.env.VUE_APP_SERVER_URL );
//   	//console.log("in created this", this)


//     //fetch( 'http://' + process.env.VUE_APP_SERVER_URL + '/get_projects?user=1')
//     fetch( 'http://localhost:5000/get_projects?user=1')
//       .then(function(response) {
//           if (!response.ok) {
//               throw Error(response.statusText);
//           }
//           return response;
//         })
//       .then(response=>response.json())
//       .then(json => {

//         console.log("in json ", json)

//         this.projects = json.projects
//       }).catch(function(error) {
//         console.log(error);
//       });

// 	}
// }
</script>