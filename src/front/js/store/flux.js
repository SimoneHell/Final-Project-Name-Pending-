const API_URL =
  "https://3001-nealxero-finalprojectna-fxjpcu5gpuq.ws-eu64.gitpod.io/";

const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      users: {
        favorites: [],

        daily_plans: [],
      },
      meals: [],
    },
    actions: {
      // Use getActions to call a function within a fuction

      loadUsers: (users) => {
        const store = getStore();

        fetch(`${API_URL}users`)
          .then((data) => data.json())
          .then(async (data) => {
            let newArray = store.users;

            newArray = newArray.concat(data);
            setStore({ users: newArray });
          });
      },

      loadMeals: (meals) => {
        const store = getStore();

        fetch(`${API_URL}meals`)
          .then((data) => data.json())
          .then(async (data) => {
            let newArray = store.meals;

            newArray = newArray.concat(data);
            setStore({ meals: newArray });
          });
      },

      loadIndivUser: (url, id, plans) => {
        const store = getStore();

        fetch(url)
          .then((data) => data.json())
          .then((data) => {
            let newArray = store[plans];
            newArray[id].info = data.result;
            setStore({ [plans]: newArray });
          });
      },

      updateFavoriteList: (newElement) => {
        const store = getStore();
        const newFavorites = [...store.users.favorites, newElement];
        setStore({ favorites: newFavorites });
      },

      deleteFavorite: (data) => {
        const store = getStore();

        let newFavorites = store.users.favorites.filter((item, i) => i != data);
        setStore({ favorites: newFavorites });
      },
    },

    getMessage: async () => {
      try {
        // fetching data from the backend
        const resp = await fetch(process.env.BACKEND_URL + "/api/hello");
        const data = await resp.json();
        setStore({ message: data.message });
        // don't forget to return something, that is how the async resolves
        return data;
      } catch (error) {
        console.log("Error loading message from backend", error);
      }
    },
  };
};

export default getState;
