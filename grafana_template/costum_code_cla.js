function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
var commndExecutionIsDone = false;
let COMMAND = '';
elements.map((element) => {
  // Check if the element's ID is "out"
  if (element.id === 'in') {
    // If the ID is "out", update its value to "WARRA"
    COMMAND = element.value;
  }
});
// Define the URL of your Flask API endpoint
const apiUrl = 'http://localhost:5000/command';
const apiOut = 'http://localhost:5000/get_output'
async function execute() {
  try {
    // Define the request options with the cmnd parameter
    const requestOptions = {
      method: 'GET',
    };

    // Make a request to the API with the defined options
    var start_at = Date.now();
    console.log("start at:", start_at);
    const clr      = await fetch(`${apiUrl}?cmnd=c`, requestOptions);
    const response = await fetch(`${apiUrl}?cmnd=${COMMAND} -s`, requestOptions);
    var ends_at = Date.now();
    console.log("ends  at:", ends_at);
    commndExecutionIsDone = true;
    console.log("res ok");
    if (response.ok) {
      // Parse the response JSON
      const data = await response.json();
      console.log('Responseeeeeeeeee:', data);
      locationService.partial({ 'var-CURRENT_WORKSHOP': data.CURRENT_WORKSHOP }, true);
      locationService.partial({ 'var-CURRENT_DOMAIN': data.CURRENT_DOMAIN }, true);
      var now = new Date();
      var dateText = now.toLocaleTimeString();
      locationService.partial({ 'var-refresh': dateText }, true);
    } else {
      // Handle non-successful responses
      console.error('Errorrr:', response.statusText);
    }
    return response;
  } catch (error) {
    //Handle network errors
    console.error('Network error:', error);
  }

}



// Function to make a request to the API
const fetchData = async () => {
  try {


    // Make a request to the API with the defined options
    const response = execute();
    // Check if the response is successful (status code 200)
    var x = 0;
    while (!commndExecutionIsDone || x != 2) {
      try {
        // Define the request options with the cmnd parameter
        const requestOptions = {
          method: 'GET',
        };

        // Make a request to the API with the defined options
        var start_at = Date.now();
        console.log("start at:", start_at);
        const response = await fetch(`${apiOut}`, requestOptions);
        var ends_at = Date.now();
        console.log("ends  at:", ends_at);
        if (response.ok) {
          // Parse the response JSON
          const data = await response.text();
          locationService.partial({ 'var-LAST_OUTPUT': data }, true);
          var now = new Date();
          //var dateText = now.toLocaleTimeString();
          //locationService.partial({ 'var-refresh': dateText }, true);
        } else {
          // Handle non-successful responses
          console.error('Errorrr:', response.statusText);
        }
        //return response;
      } catch (error) {
        //Handle network errors
        console.error('Network error:', error);
      }
      console.log("NB", x, "commndExecutionIsDone: ", commndExecutionIsDone);
      await sleep(500);
      if (!commndExecutionIsDone) {
        x = 0
      }
      else {
        x = x + 1;
      }


    }

  } catch (error) {
    //Handle network errors
    console.error('Network error:', error);
  }
};

// Call the fetchData function to make the request
fetchData();
return;
