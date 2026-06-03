import Header from "./components/header/Header";
import Footer from "./components/footer/Footer";
import { Login } from "./pages/login";
import { Signup } from "./pages/singup";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Home } from "./pages/home";
import { Details } from "./pages/Details";
import { Medialist } from "./pages/Medialist";
function App() {
  return (
    <div>
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/:mediaType/:id" element={<Details />} />
          <Route path="/list/:mediaType" element={<Medialist/>} />
        </Routes>
        <Footer />
      </Router>
    </div>
  )
}

export default App;