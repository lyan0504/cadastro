// Variáveis e seleção de elementos
const apikey = "14b50c4f657b3355b1382a6345c04452"; // 
const cityInput = document.querySelector("#city-input");
const searchBtn = document.querySelector("#search");

const cityElement = document.querySelector("#city");
const tempElement = document.querySelector("#temperature span");
const descElement = document.querySelector("#description");
const weatherIconElement = document.querySelector("#weather-icon");
const countryElement = document.querySelector("#country");
const humidityElement = document.querySelector("#humidity span");
const windElement = document.querySelector("#wind span");

// Função para obter os dados do clima
const getWeatherData = async (city) => {
    try {
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apikey}&units=metric`);
        const data = await response.json();

        // Atualiza o DOM com os dados do clima
        cityElement.textContent = data.name;
        tempElement.textContent = Math.round(data.main.temp);
        descElement.textContent = data.weather[0].description;
        weatherIconElement.src = `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
        humidityElement.textContent = `${data.main.humidity}%`;
        windElement.textContent = `${data.wind.speed} km/h`;
        
        // Obtém a bandeira do país
        countryElement.src = `https://flagsapi.com/${data.sys.country}/shiny/64.png`;
    } catch (error) {
        console.error("Erro ao obter dados do clima:", error);
        alert("Não foi possível obter os dados do clima. Verifique o nome da cidade e tente novamente.");
    }
};

// Evento de clique no botão de busca
searchBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const city = cityInput.value.trim();
    if (city) {
        getWeatherData(city);
    } else {
        alert("Por favor, insira o nome de uma cidade.");
    }
});