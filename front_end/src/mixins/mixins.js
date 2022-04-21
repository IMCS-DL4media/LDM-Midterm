//import {SERVER_URL_CONST} from "../main.js";

export const mymixin = {
    methods: {
      SERVER_URL() {
        //return "http://"+SERVER_URL_CONST+"/";
		    return "http://" + process.env.VUE_APP_SERVER_URL + "/";
      }
    }
  }