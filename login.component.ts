import { Component, OnInit } from '@angular/core';
import { MatSnackBar, MatSnackBarConfig } from '@angular/material';
import { Router } from '@angular/router';
import { LoginService } from './login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [LoginService]
})
export class LoginComponent implements OnInit {
  focus;
  focus1;
  password: any;
  user_id: any;
  constructor(private service: LoginService, private router: Router,
    private snackBar: MatSnackBar) { }

  ngOnInit() {
  }
  onSave(): void {
    const body ={
      'email': this.user_id,
      'password': this.password

    }
    this.service.postSignIn(body).subscribe(sucsess => {
      console.log(sucsess);
      if(sucsess.status){
        alert('login successfull ')
      }
    });
    console.log(this.password, this.user_id, body)
  }
}
