// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
 var firebaseConfig = {
    apiKey: "AIzaSyBr76X_Cn2L3f8TGtQigTbem5JqC30cqwE",
    authDomain: "apolo-bafc8.firebaseapp.com",
    projectId: "apolo-bafc8",
    storageBucket: "apolo-bafc8.appspot.com",
    messagingSenderId: "990356948715",
    appId: "1:990356948715:web:7b4f87f37d5a71c4f4a0ae",
    measurementId: "G-HNCEYBDGCM"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

function signOut() {
  console.log("cerrar sesión")
  firebase.auth().signOut().then(() => {
      // Sign-out successful.
      console.log('User signed out.');
      window.location.replace(document.location.origin+'/logout/');
    }).catch((error) => {
      // An error happened.
    });

}


function SingInGoogle(){
  var ui = new firebaseui.auth.AuthUI(firebase.auth());
  // let url = window.location.replace(document.location.origin+'/eventos/listar/');
  ui.start('#firebaseui-auth-container', {
    callbacks: {
      signInSuccessWithAuthResult: function (authResult, redirectUrl) {
        // User successfully signed in.
        // Return type determines whether we continue the redirect automatically
        // or whether we leave that to developer to handle.
        $('#firebaseui-auth-container').hide()
        let name = authResult.user.displayName
        let email = authResult.user.email
        let password =  authResult.user.uid

        sign_in_social(name,email,password);
        return true;
      },
    },
    signInFlow: 'popup',
    signInOptions: [
      // List of OAuth providers supported.
      {
      provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      scopes: [
        'https://www.googleapis.com/auth/contacts.readonly'
      ],
      customParameters: {
        // Forces account selection even when one account
        // is available.
        prompt: 'select_account'
      }
    },
    ],
    // tosUrl: url,
  });
}