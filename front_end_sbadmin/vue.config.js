// vue.config.js
module.exports = {
    devServer: {
      proxy: {
        "/login": {
          target: "http://back_end_1:5000/",		  
          changeOrigin: true,
          secure: false
        },
	      "/get_testing_data_silver_labels": {
          target: "http://localhost:5000",
          changeOrigin: true,
          secure: false
        }
      }
    }
  };