<template>
	<div>
		<p>Start of component Run</p> <br> 
		<p>Run details:</p>
		<p>Run start time: {{run.start_time}}</p>
		<p>Run finish time:{{run.finish_time}}</p>
		<p>List of logged messages:</p>
			<table style="width:80%">
				<caption>Logged messages : </caption>
				<thead>
					<tr>
						<th> # </th>
						<th> ID </th>
						<th> Message </th>
						
					</tr>
				</thead>
				<tbody>
					<tr v-for="log, ind in run.logs">								
						<td>{{ ind }}</td>								
						<td>{{log.id}}</td>
						<td>{{ log.msg }}</td>								
					</tr>							
				</tbody>
			</table>
		<p>List of uploaded files:</p>
			<table style="width:80%">
				<caption>Uploaded files : </caption>
				<thead>
					<tr>
						<th> # </th>
						<th> File name </th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="file, ind in run.files">								
						<td>{{ind}}</td>								
						<td> <a :href= " SERVER_URL() + 'get_file/' + file + '?run_id=' + run_id" >{{file}}</a> </td>
						
					</tr>							
				</tbody>
			</table>
		<p>Labels on data:</p> 					
		
		<p> Gold labels : </p>
		{{run.gold}}
		<p> Silver labels: </p>
		{{run.silver}}
		<p> File name, gold label, silver label : </p>
		{{run.file_gold_silver}}
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
			<div class="gallery" v-for="elem, ind in run.file_gold_silver" >
				<a target="_blank"
					:href=" SERVER_URL() + 'get_training_file/'+elem[0]+'?project_id=' + run.project_id">
					<img 
						:src=" SERVER_URL() + 'get_training_file/'+elem[0]+'?project_id=' + run.project_id" 
						width="600" height="400">
				</a>
				<div class="desc">Gold : {{elem[1]}} </div>
				<div class="desc">Silver : {{elem[2]}} </div>
			</div>

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
		<p>End of component</p> <br> 
	</div>

</template>

<script src="./Run.js"></script>