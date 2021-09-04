import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NetworkService } from 'src/app/service/network.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.scss'],
  providers: [NetworkService]
})
export class SignInComponent implements OnInit {
  constructor(private networkService: NetworkService, private router: Router) { }

  email = '';
  password =  '';
  
  
  ngOnInit(): void {
  }

  onSignInPost(): void {

    // validation

    if (this.email.length == 0) {
      alert('Please enter your email.');
      return;
    }

    if (this.password.length == 0) {
      alert('Please enter your password.');
      return;
    }

    const restBody = {
      emailAddress: this.email,
      password: this.password
    };

    console.log('main_body', restBody);

    this.networkService.postSignIn(restBody).subscribe( success => {
      console.log(success);
      if (success.status == true) {
        // sign in success
        localStorage.setItem(environment.authKey, success.result[0].Authorization);
        this.networkService.updateHeaders();
        this.router.navigate(['home']);
      } else {
        alert(success.message);
      }
      
    }, error => {

    });

  }

  onSignUp(): void {
    this.router.navigate(['sign_up']);
  }
}