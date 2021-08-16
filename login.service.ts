
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Injectable()
export class LoginService {


  constructor(private http: HttpClient) {
    
  }
  // constructor(private http: HttpClient) {
  // }

  // postSignIn(body: any): Observable<any> {
  //   return this.http.post<any>('/api/admin_sign_in', body, {
  //   });
  // }

  postSignIn(body: any): Observable<any> {

    // console.log(this.headers, body);
    return this.http.post<any>(
      'https://api.xlayer.in/julygroup6_web/api/sign/in', body, {
      // headers: this.headers
    });
  }
  postSignUp(body: any): Observable<any> {

    // console.log(this.headers, body);
    return this.http.post<any>(
      'https://api.xlayer.in/julygroup6_web/api/sign/up', body, {
      // headers: this.headers
    });
  }

}
