<template>
 	<div>
		<p>Start of component Project</p> <br> 
		
		<p>Project {{ project_id }} </p>
		
		<button disabled> Data </button> 
		<button disabled> Runs </button> <br>
		
		Training data set:
		
		<a 
            :href= " SERVER_URL() + 'get_training_set?project_id=' + project_id + 
            '&file_name=' + training_data_download_link "> 
            {{training_data_download_link}}
        </a>
		
		
		<table style="width:80%">
			<caption>Runs : </caption>
			<thead>
				<tr>
					<th> # </th>
					<th> ID </th>
					<th> Start datetime </th>
					<th> End  datetime </th>
					<th> Final accuracy </th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="run, ind in runs">								
					<td>{{ ind }}</td>
					
					<td><router-link :to="'/run/' + run.id" >{{run.id}}</router-link></td>
					<td>{{ run.start_time }}</td>
					<td>{{ run.finish_time }}</td>								
					<td>97</td>
				</tr>
				
			</tbody>
		</table>
				
		<p>End of component</p> <br> 
	</div>
</template>

<script src="./Project.js"></script>