<template>
    <div>
<div class ="container">
        <!-- ProjectID : {{project_id}} -->
        <div class="col-sm-3 offset-sm-9">
                    <!-- {{runs}} -->
                    <div class="form-group form-inline">
                      <label for="sel1" class = "my-1 mr-2" >Select run :  </label>
                      <select class="form-control my-1 mr-2 form-control-sm" id="sel1" v-model="currentRunId"  @change="runChanged()">
                        <option v-for="run in runs" :value="run.id"> {{run.id}}</option>
                    <!--     <option> 1</option>
                        <option> 2</option>
                        <option> 3</option>
                        <option> 4</option> -->
                      </select>
                    </div> 
                
        </div>

        <div v-if="!isLoading" class="row">
            <div class = "col-sm-3 ">
				<!--
					Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
				-->
                    <!-- <br/> -->
                    <!-- List of checboxes -->
					<div class = "font-weight-bolder h5">Gold labels:</div>
					<!-- <br/> -->
					
                    <!--<br/> -->
                    <!-- <input type="checkbox" disabled> ClassName 1<br/>
                    <input type="checkbox" disabled> ClassName 2<br/>
                    <input type="checkbox" disabled> ClassName 3<br/>
                    <input type="checkbox" disabled> ClassName 4<br/>
					<br/> -->
					

                    <div v-for="cl in Object.keys(this.training_data_labels)" :key="cl">
                        <span :class="{'font-weight-bolder h5':currClassName == cl}">
                            <input type="checkbox" :id="'id' + cl" checked @click = "checkboxClicked( cl, 'id' + cl )">                             
                                {{cl}}                            
                                ({{"G: " + training_data_labels[cl].length + " / S: " + ( testing_data_silver_labels[cl] ? testing_data_silver_labels[cl].length : "0") }}) <br/>
                        </span>
                    </div>
                    <br/>
                    <button type="button" class="btn btn-secondary mr-2" @click="selectAllCheckboxes()">Select all</button>
                    <button type="button" class="btn btn-secondary"  @click="clearAllCheckboxes()">Clear all</button>
                    <br/>
                    <br/>
					<!-- Silver labels:
					<br/>
					<br/> -->
                    <!-- <div v-for="cl in this.classes.keys()" :key="cl">
                        <input type="checkbox" :id="'id' + cl" checked @click = "checkboxClicked( cl, 'id' + cl )" > {{cl}} <br/>
                    </div> -->
                    <!-- <br/> -->

                    <div class = "font-weight-bolder h5">Filter :</div>
					<!-- <br/> -->
                    
						<div class="form-group ">
							<!-- <label for="fset1">Show : </label> -->
							<fieldset id="fset1"  @change="filterModeChanged()"  >
                                <!-- <legend>Binding : </legend> -->
                                <div class="form-check-inline">
									<label class="form-check-label" >
										<input class="form-check-input" type="radio" name="binding" id="binding_provided" value="All" checked v-model="filter_mode" disabled="disabled"> All
									</label>
								</div>
								<br/>
								<div class="form-check-inline">
									<label class="form-check-label" >
										<input class="form-check-input" type="radio" name="binding" id="binding_weak" value="Matching" v-model="filter_mode" disabled="disabled"> Matching (Gold == Silver)
									</label>
								</div>
                                <br/>
								<div class="form-check-inline">
									<label class="form-check-label" >
										<input class="form-check-input" type="radio" name="binding" id="binding_strong" value="Mismatching" v-model="filter_mode" disabled="disabled"> Mismatching (Gold != Silver)
									</label>
								</div>
                                
								
							</fieldset>
						</div>
                    
            </div>
    
            <div class = "col-sm-9">
                <!--
					Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
				-->
                <!-- <br/> -->
                
                
                <div class = "row" >
                    <div class = "col" v-for="p in this.currChunkData1">
                        <img height = "150" width = "150" :src=" SERVER_URL() + 'get_testing_file/' + p + `?project_id=` + project_id "  >
                        <div> <span class = "font-weight-bolder h6" >Gold label : </span>{{currClassName}}</div>
                        <div> 
                                <span  :class="{'text-danger':currClassName != file_2_label[p] , 'text-success':currClassName == file_2_label[p]}">
                                    <span class = "font-weight-bolder "  >Silver label :</span> 
                                
                                    {{file_2_label[p] ? file_2_label[p] : "Unknown" }} 
                                </span>
                        </div>
                        <div class="mb-3"> <span class = "font-weight-bolder" >File name : </span>{{p}}</div>
                    </div>
                </div>
<!-- 
                <div class = "row" >
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
                        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>
                    </div>
                
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
                        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>
                    </div>
                
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>                
                    </div>
                    
                    <div class = "col">
                        <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
                        alt="Smiley face" height="150" width="150">
                        
                        <div>Gold label : Sunflower</div>
                        <div>Silver label : Sunflower</div>
                    </div>
                
					<div class="col">
						<img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg" 
						alt="Smiley face" height="150" width="150">
						
						<div>Gold label : Sunflower</div>
						<div>Silver label : Sunflower</div>
					</div>

					
                
                </div> -->
                
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                <!-- <img src="https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/helianthus_suncredible_yellow_01.jpg"  -->
                <!-- alt="Smiley face" height="150" width="150"> -->
                
				
				
					<!-- <nav aria-label="Page navigation example" >
                        <ul class="pagination justify-content-center">
                            <li class="page-item"><a class="page-link" href="#" >Previous</a></li>
                            <li class="page-item"><a class="page-link" href="#">1</a></li>
                            <li class="page-item"><a class="page-link" href="#">2</a></li>
                            <li class="page-item"><a class="page-link" href="#">3</a></li>
                            <li class="page-item"><a class="page-link" href="#">Next</a></li>
                        </ul>
					</nav> -->

                <br/>
                
                <div class ="row justify-content-center">
                    <button @click="prevPage1" :disabled=" canMoveBackward().isPossible != true" class="btn btn-secondary mr-1"> <- Previous </button>
                    <button @click="nextPage1" :disabled=" canMoveForward().isPossible != true" class="btn btn-secondary">Next -> </button>
                </div>
				
            </div>
        </div>
    </div>
    </div>
</template>

<script src="./TestDataViewer1.js"></script>