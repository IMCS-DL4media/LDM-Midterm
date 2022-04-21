let timer;


export default {
  async login(context, payload) {
    return context.dispatch('auth', {
      ...payload,
      mode: 'login'
    });
  },
  async signup(context, payload) {
    return context.dispatch('auth', {
      ...payload,
      mode: 'signup'
    });
  },
  async auth(context, payload) {
    const mode = payload.mode;
    let url = "/login/";

    const response = await fetch(url, {
      method: 'POST',
      //mode: 'no-cors',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: payload.email,
        password: payload.password,
        user_id: payload.email,
        user_psw_hash: payload.password
      })
    });
    
    console.log(response)
    const responseData = await response.json();
    console.log("respone data ", responseData)

    if (!response.ok) {
      const error = new Error(
        responseData.message || 'Failed to authenticate. Check your login data.'
      );
      throw error;
    }

    //const expiresIn = +responseData.expiresIn * 1000;
    const expiresIn = 5000 * 1000;
    const expirationDate = new Date().getTime() + expiresIn;

    localStorage.setItem('token', responseData.token);
    localStorage.setItem('userId', responseData.user_id);
    localStorage.setItem('userName', responseData.user_name);
    localStorage.setItem('tokenExpiration', expirationDate);

    timer = setTimeout(function() {
      context.dispatch('autoLogout');
    }, expiresIn);

    context.commit('setUser', {
      token: responseData.token,
      userId: responseData.user_id,
      userName: responseData.user_name
    });
  },

  tryLogin(context) {
    const token = localStorage.getItem('token');
    const userId = localStorage.getItem('userId');
    const userName = localStorage.getItem('userName');
    const tokenExpiration = localStorage.getItem('tokenExpiration');

    const expiresIn = +tokenExpiration - new Date().getTime();

    if (expiresIn < 0) {
      return;
    }

    timer = setTimeout(function() {
      context.dispatch('autoLogout');
    }, expiresIn);

    if (token && userId) {
      context.commit('setUser', {
        token: token,
        userId: userId,
        userName: userName
      });
    }
  },

  logout(context) {
    localStorage.removeItem('token');
    localStorage.removeItem('userId');
    localStorage.removeItem('userName');
    localStorage.removeItem('tokenExpiration');

    clearTimeout(timer);

    context.commit('setUser', {
      token: null,
      userId: null,
      userName: null
    });
  },

  autoLogout(context) {
    context.dispatch('logout');
    context.commit('setAutoLogout');
  }
};
