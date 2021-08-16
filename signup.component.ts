import { Component, OnInit } from '@angular/core';
import { MatSnackBar, MatSnackBarConfig } from '@angular/material';
import { Router } from '@angular/router';
import { LoginService } from '../login/login.service';

@Component({
    selector: 'app-signup',
    templateUrl: './signup.component.html',
    styleUrls: ['./signup.component.scss'],
    providers: [LoginService]
})
export class SignupComponent implements OnInit {
    focus;
    focus1;
    password: any;
    user_id: any;
    firstName: any;
    lastName: any;
    phoneNumber: any;
    constructor(private service: LoginService, private router: Router,
        private snackBar: MatSnackBar) { }

    ngOnInit() {
    }
    onSave(): void {
        const body = {
            email: this.user_id,
            password: this.password,
            firstName: this.firstName,
            lastName: this.lastName,
            phoneNumber: this.phoneNumber,


        }
        this.service.postSignUp(body).subscribe(sucsess => {
            console.log(sucsess);
            if (sucsess.status) {
                alert('login successfull ')
            }
        });
        console.log(this.password, this.user_id, body)
    }
}
