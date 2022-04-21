<template>
	<div>
		<!-- <p>Start of component Run</p> <br> -->
		
		
		<!-- <p>Run start time : {{run.start_time}} </p>
		<p>Run finish time : {{run.finish_time}} </p>
		<p>Comment : {{run.comment}} </p>
		<p>Commit URL : <a :href="run.git_commit_url">{{run.git_commit_url}}</a></p> -->

			<div class="card shadow mb-4">
				<div class = "card-header py-3">
					<h6 class="m-0 font-weight-bolder text-primary">Run properties:</h6>
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
							<label class="col-sm-2 text-right font-weight-bold">Run ID : </label>
							<label class="col-sm-4">{{run_id}}</label>							
						</div>
						<div class="form-row">
							<label class="col-sm-2 text-right font-weight-bold">Run start time : </label>
							<label class="col-sm-4">{{run.start_time}}</label>							
						</div>
						<div class="form-row">
							<label class="col-sm-2 text-right font-weight-bold">Run finish time : </label>
							<label class="col-sm-4">{{run.finish_time}}</label>							
						</div>
						<div class="form-row">
							<label class="col-sm-2 text-right font-weight-bold">Comment : </label>
							<label class="col-sm-4">{{run.comment}}</label>							
						</div>
						<div class="form-row">
							<label class="col-sm-2 text-right font-weight-bold">Commit URL : </label>
							<label class="col-sm-9"><a :href="run.git_commit_url">{{run.git_commit_url}}</a></label>							
						</div>
						<div class="form-row">
							<label class="col-sm-2 text-right font-weight-bold">Run author : </label>
							<label class="col-sm-4"> user1 </label>							
						</div>
					</form>

				</div>
			</div>
		

		<div class="card shadow mb-4">
            <div class="card-header py-3">
              <h6 class="m-0 font-weight-bold text-primary">Logged messages:</h6>
            </div>
			
		<div class = "card-body">
		
		
		<!-- <p>List of logged messages:</p> -->
		<div class="table-responsive">
                <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
			
				<!-- <caption>Logged messages : </caption> -->
				<thead>
					<tr>
						<th> # </th>
						<th> Role name </th>
						<th> Message ID </th>
						<th> Message </th>
						<th> Logged on </th>
						
					</tr>
				</thead>
				<!-- <tfoot>
					<tr>
						<th> # </th>
						<th> Message ID </th>
						<th> Message </th>
						<th> Logged on </th>
					</tr>
				</tfoot> -->
				<tbody>
					<tr v-for="(log, ind) in run.logs" :key="log.id">
						<td>{{ ind }}</td>
						<td>{{ log.role_name }} </td>
						<td>{{ log.id }}</td>
						<td>{{ log.msg }}</td>
						<td>{{ log.logged_on }}</td>
					</tr>
				</tbody>
			</table>

		</div>
	</div>
	</div>

	
		<div class="card shadow mb-4">
            <div class="card-header py-3">
              <h6 class="m-0 font-weight-bold text-primary">Uploaded files:</h6>
            </div>
		<!-- <p>List of uploaded files:</p> -->
		<div class = "card-body">
		<div class="table-responsive">
			<table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
				<!-- <caption>Uploaded files : </caption> -->
				<thead>
					<tr>
						<th> # </th>
						<th> Role name </th>
						<th> File name </th>
						<th> Upload time </th>
						<th> Comment </th>
					</tr>
				</thead>
				<!-- <tfoot>
					<tr>
						<th> # </th>
						<th> File name </th>
						<th> Upload time </th>
						<th> Comment </th>
					</tr>
				</tfoot> -->
				<tbody>
					<tr v-for="(file, ind) in run.files" :key="file.file_name">
						<td>{{ind}}</td>
						<td> {{file.role_name}} </td>
						<td> <a :href= " SERVER_URL() + 'get_file/' + file.file_name + '?run_id=' + run_id" >{{file.file_name}}</a> </td>
						<td> {{file.upload_time}} </td>
						<td> {{file.comment}} </td>
					</tr>
				</tbody>
			</table>
		</div>
		</div>
		</div>

		<!-- <p>Labels on data:</p> 					
		
		<p> Gold labels : </p>
		{{run.gold}}
		<p> Silver labels: </p>
		{{run.silver}}
		<p> File name, gold label, silver label : </p>
		{{run.file_gold_silver}} -->
	<!-- 					
			<table style="width:80%">
				<caption>Training files : </caption>
				<thead>
					<tr>
						<th> # </th>
						<th> File name </th>
						<th> Gold </th>
						<th> Silver </th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="elem, ind in run.file_gold_silver">								
						<td>{{ind}}</td>								
						<td><img :src=" SERVER_URL() + 'get_training_file/'+elem[0]+'?project_id=' + run.project_id"></td>
						<td>{{elem[1]}}</td>
						<td>{{elem[2]}}</td>
						
					</tr>							
				</tbody>
			</table> -->
		
		<div>


			<!-- <div class="gallery" v-for="elem, ind in run.file_gold_silver" >
				<a target="_blank"
					:href=" SERVER_URL() + 'get_training_file/'+elem[0]+'?project_id=' + run.project_id">
					<img 
						:src=" SERVER_URL() + 'get_training_file/'+elem[0]+'?project_id=' + run.project_id" 
						width="600" height="400">
				</a>
				<div class="desc">Gold : {{elem[1]}} </div>
				<div class="desc">Silver : {{elem[2]}} </div>
			</div> -->

			<!-- <div class="gallery">
			<a target="_blank" href="img_forest.jpg">
				<img src="img_forest.jpg" alt="Forest" width="600" height="400">
			</a>
			<div class="desc">Add a description of the image here</div>
			</div>

			<div class="gallery">
			<a target="_blank" href="img_lights.jpg">
				<img src="img_lights.jpg" alt="Northern Lights" width="600" height="400">
			</a>
			<div class="desc">Add a description of the image here</div>
			</div>

			<div class="gallery">
			<a target="_blank" href="img_mountains.jpg">
				<img src="img_mountains.jpg" alt="Mountains" width="600" height="400">
			</a>
			<div class="desc">Add a description of the image here</div>
			</div> -->
		</div>
		<!-- <p>End of component</p> <br>  -->
	</div>

</template>

<script src="./Run.js"></script>