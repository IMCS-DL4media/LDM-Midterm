<template>
	<div>
		
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
		<!-- The Modal -->
		<div class="modal" id="myModal">
			<div class="modal-dialog">
				<div class="modal-content">

					<!-- Modal Header -->
					<div class="modal-header">
						<h4 class="modal-title">Upload testing data set ... </h4>
						<button type="button" class="close" data-dismiss="modal">&times;</button>
					</div>

					<!-- Modal body -->
					<div class="modal-body">
										
							<!-- <div class="form-group">
								<label for="exampleInputEmail1">Project name:</label>
								<input type="text" class="form-control" id="project_name_id" aria-describedby="emailHelp" placeholder="Enter project name ... ">
								
							</div> -->

							<!-- <div class="form-group">
								<label for="exampleInputEmail1">Project type:</label>
								<select class="form-control" id = "project_type" disabled >
									<option value = "ImgClassification"> Image Classification</option>
									<option value = "ImgCaptioning"> Image Captioning</option>
								</select>
								
							</div> -->
											
							<!-- <div class="form-group">
								<label for="exampleInputEmail1">Project description:</label>
								<input type="text" class="form-control" id="project_description_id" aria-describedby="emailHelp" placeholder="Enter project description ... ">
								
							</div> -->

							
							<div class="form-group" >
								<label for="exampleInputEmail1">Testing data set file:</label>
								<div class="file-loading">
									<input id="test_file_input_id" name="test_file_input" type="file" ref="fileInputRef" accept=".zip">
								</div>	
							</div> 
							
							
					</div>

					<!-- Modal footer -->
					<div class="modal-footer">
						<button type="button" class="btn btn-primary" data-dismiss="modal" @click="uploadTestDataSetClicked">Upload</button>
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
					</div>

				</div>
			</div>
		</div>

		<!-- The Modal -->
		<div class="modal" id="train_data_modal">
			<div class="modal-dialog">
				<div class="modal-content">

					<!-- Modal Header -->
					<div class="modal-header">
						<h4 class="modal-title">Upload training data set ... </h4>
						<button type="button" class="close" data-dismiss="modal">&times;</button>
					</div>

					<!-- Modal body -->
					<div class="modal-body">
										
							<!-- <div class="form-group">
								<label for="exampleInputEmail1">Project name:</label>
								<input type="text" class="form-control" id="project_name_id" aria-describedby="emailHelp" placeholder="Enter project name ... ">
								
							</div> -->

							<!-- <div class="form-group">
								<label for="exampleInputEmail1">Project type:</label>
								<select class="form-control" id = "project_type" disabled >
									<option value = "ImgClassification"> Image Classification</option>
									<option value = "ImgCaptioning"> Image Captioning</option>
								</select>
								
							</div> -->
											
							<!-- <div class="form-group">
								<label for="exampleInputEmail1">Project description:</label>
								<input type="text" class="form-control" id="project_description_id" aria-describedby="emailHelp" placeholder="Enter project description ... ">
								
							</div> -->

							
							<div class="form-group" >
								<label for="exampleInputEmail1">Training data set file:</label>
								<div class="file-loading">
									<input id="test_file_input_id" name="test_file_input" type="file" ref="train_data_fileInputRef" accept=".zip">
								</div>	
							</div> 
							
							
					</div>

					<!-- Modal footer -->
					<div class="modal-footer">
						<button type="button" class="btn btn-primary" data-dismiss="modal" @click="uploadTrainingDataSetClicked">Upload</button>
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
					</div>

				</div>
			</div>
		</div>




		<!-- <p>Start of component Project</p> <br>  -->
		<!-- 		
		<p>Project ID : {{ project_id }} </p>
		<p>Project name : {{name}} </p>
		<p>Project description : {{description}} </p>
		-->
		<!-- 
			<button disabled> Data </button> 
			<button disabled> Runs </button> <br>
		-->

		<div class="container_tabs_pills">			
			<ul class="nav nav-pills">
				<li class="nav-item">
					<a class="nav-link active"  role="tab" data-toggle="tab" href="#tab-project-runs">Runs</a>
				</li>
				<li class="nav-item">
					<a class="nav-link"  role="tab" data-toggle="tab" href="#tab-data">Data</a>
				</li>
				<li class="nav-item">
					<a class="nav-link"  role="tab" data-toggle="tab" href="#tab-project-properties">Project properties</a>
				</li>			
			</ul>
			<div class="tab-content">
				<div class="tab-pane fade active show" id="tab-project-runs">
					<br/>
					<div class="card shadow mb-4">
						<div class="card-header py-3">
							<h6 class="m-0 font-weight-bold text-primary">Project runs : </h6>
						</div>
						<div class="card-body">
							<div class="table-responsive">
								<table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
									<!-- <caption>Runs : </caption> -->
									<thead>
										<tr>
											<th> # </th>
											<th> Run ID </th>
											<th> Comment </th>
											<th> Start datetime </th>
											<th> End  datetime </th>
											<th> IP </th>
											<th> User ID </th>
											<th> Commit URL </th>
										</tr>
									</thead>
									<!-- <tfoot>
										<tr>
											<th> # </th>
											<th> Run ID </th>
											<th> Comment </th>
											<th> Start datetime </th>
											<th> End  datetime </th>
											<th> IP </th>
											<th> User ID </th>
											<th> Commit URL </th>
										</tr>
									</tfoot> -->
									<tbody>
										<tr v-for="(run, ind) in runs" :key="run.id">								
											<td>{{ ind }}</td>
											
											<td><router-link :to="'/run/' + run.id" >{{run.id}}</router-link></td>
											<td>{{get_first_10_symb( run.comment ) + " ..." }}</td>
											<td>{{ run.start_time }}</td>
											<td>{{ run.finish_time }}</td>								
											<!-- <td>97</td> -->
											
											<td> {{run.remote_address}}</td>
											<td> user1 </td>
											<td> <a :href="run.git_commit_url"> {{run.git_commit_url_shortened}} </a> </td>
										</tr>
										
									</tbody>
								</table>
							</div>
						</div>
					</div>
				</div>

				<div class="tab-pane fade" id="tab-data">
					<br/>
					<div class = "row">
						<div class = "card shadow mb-4 col ml-2 mr-2"> 
							<div class = "card-header py-3">
								<h6 class="m-0 font-weight-bold text-primary">Test data set:</h6>
							</div>
							
							<div class="card-body">
								<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal"  
									v-if="!(testing_data_download_link != null && testing_data_download_link.length > 0)" >
									Upload testing data ...
								</button>
								<div v-else>
									<form class="form-horizontal">						
										<div class="form-row">
											<label class="col-sm-2 text-right font-weight-bold">File name : </label>
											<label class="col-sm-4">{{testing_data_download_link}}</label>							
										</div>
										<div class="form-row">
											<label class="col-sm-2 text-right font-weight-bold">File size : </label>
											<label class="col-sm-4">{{testing_file_size}}</label>							
										</div>
									</form>
									<!-- File name : {{testing_data_download_link}} <br/>
									File size : {{testing_file_size}} <br/>				 -->
									<br/>
									<div class = "tpbutton btn-toolbar text-center">
										<a class = "btn btn-primary btn-sm  mr-2"
											:href= " SERVER_URL() + 'get_testing_set?project_id=' + project_id + 
											'&file_name=' + testing_data_download_link "> 
											<i class = "fas fa-download fa-sm text-white-50"></i>
											Download testing set 
											<!-- {{training_data_download_link}} -->
										</a>
										<!-- <br/>
										<br/> -->

										<!-- <router-link :to="'/ViewTestData/' + project_id " class = "btn btn-primary btn-sm " disabled>
											<i class = "fas fa-eye fa-sm text-white-50"></i>
											Explore testing set 
										</router-link> -->
										<!-- <button class = "btn btn-primary btn-sm " disabled>
											<i class = "fas fa-eye fa-sm text-white-50"></i>
											Explore testing set 
										</button> -->
										<!-- <router-link :to="'/ViewTestData1/' + project_id " class = "btn btn-primary btn-sm " >
											<i class = "fas fa-eye fa-sm text-white-50"></i>
											Explore testing set 
										</router-link> -->
										<router-link :to="{ name: 'TestDataViewer1', params: { project_id: project_id, runs: runs } }" 
													 class = "btn btn-primary btn-sm " >
											<i class = "fas fa-eye fa-sm text-white-50"></i>
											Explore testing set 
										</router-link>
									</div>
								</div>
							</div>
						</div>
					
						<div class = "card shadow mb-4 col mr-2"> 
							<div class = "card-header py-3">
								<h6 class="m-0 font-weight-bold text-primary">Training data set:</h6>
							</div>
							
							<div class="card-body">
								<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#train_data_modal"  
									v-if="!(training_data_download_link != null && training_data_download_link.length > 0)" >
									Upload training data ...
								</button>
								<div v-else>
									<form class="form-horizontal">						
										<div class="form-row">
											<label class="col-sm-2 text-right font-weight-bold">File name : </label>
											<label class="col-sm-4">{{training_data_download_link}}</label>							
										</div>
										<div class="form-row">
											<label class="col-sm-2 text-right font-weight-bold">File size : </label>
											<label class="col-sm-4">{{training_file_size}}</label>							
										</div>
									</form>
									<!-- File name : {{training_data_download_link}} <br/>
									File size : {{training_file_size}} <br/>				 -->
									<br/>
									<div class = "tpbutton btn-toolbar text-center">
										<a class = "btn btn-primary btn-sm  mr-2"
											:href= " SERVER_URL() + 'get_training_set?project_id=' + project_id + 
											'&file_name=' + training_data_download_link "> 
											<i class = "fas fa-download fa-sm text-white-50"></i>
											Download training set 
											<!-- {{training_data_download_link}} -->
										</a>
										<!-- <br/>
										<br/> -->

										<router-link :to="'/ViewTestData/' + project_id " class = "btn btn-primary btn-sm " >
											<i class = "fas fa-eye fa-sm text-white-50"></i>
											Explore training set 
										</router-link>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				
				<div class="tab-pane fade" id="tab-project-properties">
					<br/>
					<div class="card shadow mb-4 ml-2 mr-2 col">
						<div class = "card-header py-3">
							<h6 class="m-0 font-weight-bolder text-primary">Properties:</h6>
						</div>
						<div class = "card-body">
							<!-- <p>Project name : {{name}} </p>
							<p>Project ID : {{ project_id }} </p>				
							<p>Project description : {{description}} </p>
							<p>Created on : ... </p>
							<p>Owner : ... </p>
							-->
							<form class="form-horizontal">						
								<div class="form-row">
									<label class="col-sm-1 text-right font-weight-bold">Name : </label>
									<label class="col-sm-4">{{name}}</label>							
								</div>
								<div class="form-row">
									<label class="col-sm-1 text-right font-weight-bold">ID : </label>
									<label class="col-sm-4">{{ project_id }}</label>							
								</div>
								<div class="form-row">
									<label class="col-sm-1 text-right font-weight-bold">Description : </label>
									<label class="col-sm-4">{{description}}</label>							
								</div>
								<div class="form-row">
									<label class="col-sm-1 text-right font-weight-bold">Created on : </label>
									<label class="col-sm-4">{{created_at}}</label>							
								</div>
								<div class="form-row">
									<label class="col-sm-1 text-right font-weight-bold">Owner : </label>
									<label class="col-sm-4"> user1 </label>							
								</div>
							</form>

						</div>
					</div>
				</div>
			</div>
		</div>


	</div>
</template>

<script src="./Project.js"></script>