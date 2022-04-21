<template>
	<div>
		<p>Start223 of component ListOfProjects</p> 	
		<p>List of projects : {{user_id}} </p>
		<!--
		<p>List of projects  : {{this.$parent.projects}} </p>
		-->
		<ul>
			<li v-for="proj in this.$parent.$parent.projects" v-bind:key="proj.id"> 			
				
				<router-link :to="'/project/' + proj.id" >{{proj.name}}</router-link>							
			</li>
		</ul>
						
		<!-- <table style="width:80%; border:0px">
			<caption>List of projects : </caption>
			<thead>
				<tr>									
					<th> Project name </th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="proj in this.$parent.$parent.projects">															
					<td> <router-link :to="'/project/' + proj.id" >{{proj.name}}</router-link>	 </td>
				</tr>							
			</tbody>
		</table> -->


		<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">Create new project ...</button>

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

		<p>End of component ListOfProjects</p> 

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
						<input type="text" class="form-control" id="project_name_id" aria-describedby="emailHelp" placeholder="Enter project name">
						
					</div>

					<div class="form-group">
						<label for="exampleInputEmail1">Training data file:</label>
						<div class="file-loading">
							<input id="training_file_input_id" name="training_file_input" type="file" ref="fileInputRef" >
						</div>	
					</div>
					
		      </div>

		      <!-- Modal footer -->
		      <div class="modal-footer">
				<button type="button" class="btn btn-primary" data-dismiss="modal" @click="createNewProjectClicked">Create</button>
		        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
		      </div>

		    </div>
		  </div>
		</div>

		<p>ABC</p>

	</div>

</template>

<script src="./Projects.js"></script>