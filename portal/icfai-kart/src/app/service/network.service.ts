import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class NetworkService {

  headers: any = {};

  constructor(private httpHandler: HttpClient) { }

  postSignIn(body: any): Observable<any> {
    return this.httpHandler.post<any>(environment.serverUrl + '/sign_in', body, {});
  }

  postSignUp(body: any): Observable<any> {
    return this.httpHandler.post<any>(environment.serverUrl + '/sign_up', body, {});
  }

  postProduct(body: any): Observable<any> {
    this.updateHeaders();
    return this.httpHandler.post<any>(environment.serverUrl + '/product', body, {
      headers: this.headers,
    },
    );
  }

  getProduct(): Observable<any> {
    this.updateHeaders();
    return this.httpHandler.get<any>(environment.serverUrl + '/product', {
      headers: this.headers,
    },
    );
  }

  updateHeaders() {
    const aKey = localStorage.getItem(environment.authKey);
    this.headers = {
      Authorization: 'Bearer ' + aKey
    };
  }

}
