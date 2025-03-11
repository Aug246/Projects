import { useEffect } from 'react';
import Homebar from '../components/Homebar';
import LoginField from '../components/LoginField';

function App() {
  useEffect(() => {
    console.log("Initializing CSRF token.....");
    
    fetch("https://0a79-47-22-173-162.ngrok-free.app/login/health_check/", {
      method: "GET", // Ensure credentials are sent with the request
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json(); 
    })
    .then(data => {
      console.log("CSRF token initialized successfully:", data);
    })
    .catch(error => {
      console.error("Error initializing CSRF token:", error);
    });
  }, []); // Empty dependency array means this will run only once when the component mounts

  return (
    <>
      <Homebar/>
      <LoginField/>
    </>
  );
}

export default App;
