const API_URL =
  "https://3001-simonehell-finalproject-49aiay3q1gu.ws-us67.gitpod.io/"

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

      loadIndivMeal: (url, id, plans) => {
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

  };
};

export default getState;