import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NetworkService } from 'src/app/service/network.service';
import { environment } from 'src/environments/environment';
@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss'],
   providers: [NetworkService]
})
export class SignUpComponent implements OnInit {

  constructor(private networkService: NetworkService,private router: Router) {} 

  firstName: String = '';
  lastName: String = '';
  phoneNumber: String = '';
  email: String = '';
  password: String = '';

 

  ngOnInit(): void {
  }
  onSignIn() {
    this.router.navigate(['sign_in']);
  }



 onSignUpPost(): void {

    // validation

    if (this.firstName.length == 0) {
      alert('Please enter your firstName.');
      return;
    }
      if (this.lastName.length == 0) {
      alert('Please a valid lastName.');
      return;
    }

    
    if (this.phoneNumber.length == 0) {
      alert('Please enter your phoneNumber.');
      return;
    }

    if (this.email.length == 0) {
      alert('Please a valid email.');
      return;
    }

    if (this.password.length == 0) {
      alert('Please enter your password.');
      return;
    }

    const restBody = {
      firstName: this.firstName,
      lastName: this.lastName,
      phoneNumber: this.phoneNumber,
      emailAddress: this.email,
      password: this.password
    };

    console.log('main_body', restBody);

    this.networkService.postSignUp(restBody).subscribe( success => {
      console.log(success);
      if (success.status == true) {
        // sign up success
        localStorage.setItem(environment.authKey, success.result[0].Authorization);
        this.router.navigate(['home']);
      } else {
        alert(success.message);
      }

    }, error => {

    });

}






}
